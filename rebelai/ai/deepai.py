#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""deepai models"""

import random
import typing
from hashlib import md5

import aiohttp

from .. import const, enums


async def deepai(
    model: enums.DeepAIModel,
    data: typing.Dict[str, typing.Any],
    api_key: typing.Optional[str] = None,
    user_agent: str = const.DEFAULT_DEEPAI_USER_AGENT,
    headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
    api: str = const.DEFAULT_DEEPAI_API,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
    session_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> typing.Dict[str, typing.Any]:
    """multiple deepai model access ( proxies highly suggested )

    *model(..enums.DeepAIModel): the deepai model you're using
    *data(dict[str, Any]): the form posted to the api ( usually 'text' for prompts )
    api_key(str | None): optional api key to use, otherwise it's generated automatically
    user_agent(str): user agent posted in the headers
    headers(dict[str, Any] | None): any other headers
    api(str): the deepai api url
    request_args(dict[str, Any] | None): arguments passed to `session.post()`
    session_args(dict[str, Any] | None): arguments passed to `aiohttp.ClientSession()`

    return(dict[str, Any]): the ai api response as json, `output` is what you're
                            looking for usually"""

    if api_key is None:

        def rev_md5(val: str) -> str:
            return md5(val.encode()).hexdigest()[::-1]

        k: int = round(1e11 * random.random())
        api_key = f"tryit-{k}-\
{rev_md5(user_agent + rev_md5( user_agent + rev_md5(user_agent + str(k) + 'x')))}"

    async with aiohttp.ClientSession(**(session_args or {})) as session:
        async with session.post(
            url=f"{api}/{model.value}",
            headers={"api-key": api_key, "user-agent": user_agent, **(headers or {})},
            **(request_args or {}),
            data=data,
        ) as response:
            return await response.json()
