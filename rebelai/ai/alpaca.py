#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""alpaca models"""

import typing

import aiohttp

from .. import const


async def alpaca_7b(
    prompt: str,
    api: str = const.DEFAULT_ALPACA_7B_API,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
    session_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> typing.Optional[str]:
    """alpaca generation model ( 7 bilion neuron ) access

    *prompt(str): the prompt passed to the ai
    api(str): api url for the alpaca model
    request_args(dict[str, Any] | None): arguments passed to `session.post()`
    session_args(dict[str, Any] | None): arguments passed to `aiohttp.ClientSession()`

    return(str | None): the ai output as a string or nothing if no output was
                        generated"""

    async with aiohttp.ClientSession(**(session_args or {})) as session:
        async with session.post(
            url=api,
            json={"prompt": prompt},
            **(request_args or {}),
        ) as response:
            return (await response.json()).get("completion")
