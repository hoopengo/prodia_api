#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pollinations image ai"""

import random
import typing

import aiohttp

from .. import const


async def pollinations(
    prompt: str,
    api: str = const.DEFAULT_POLLINATIONS_API,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
    session_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> bytes:
    """pollinations generation model access ( proxies suggested + watermark )

    *prompt(str): the prompt passed to the ai
    api(str): api url for the alpaca model
    request_args(dict[str, Any] | None): arguments passed to `session.get()`
    session_args(dict[str, Any] | None): arguments passed to `aiohttp.ClientSession()`

    return(bytes): jpeg image as bytes"""

    async with aiohttp.ClientSession(**(session_args or {})) as session:
        async with session.get(
            url=f"{api}/{prompt}{random.randint(0, 9999999999999)}",
            **(request_args or {}),
        ) as response:
            return await response.read()
