#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""inferkit model"""

import json
import typing

import aiohttp

from .. import const


async def standard(
    prompt: str,
    api: str = const.DEFAULT_INFERKIT_STARNDARD_API,
    no_end: bool = True,
    keywords: typing.Optional[typing.List[str]] = None,
    length: int = const.DEFAULT_INFERKIT_LEN,
    continuation: bool = False,
    begining: bool = True,
    temperature: float = const.DEFAULT_INFERKIT_TEMP,
    probability: float = const.DEFAULT_INFERKIT_PROB,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
    session_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> typing.Optional[str]:
    """inferkit standard completion model access ( proxies suggested )

    *prompt(str): the prompt passed to the ai
    no_end(bool): pauses when neural network it should end
    keywords(list[str] | None): list of required words
    length(int): maximum number of characters to be generated
    continuation(bool): is continuation
    begining(bool): should prompt be treated as beginning of the document
    temperature(float): randomness and creativity
    probability(float): probability of discarding unlikely text in the sampling process
    api(str): api url for the alpaca model
    request_args(dict[str, Any] | None): arguments passed to `session.post()`
    session_args(dict[str, Any] | None): arguments passed to `aiohttp.ClientSession()`

    return(str | None): the ai output as a string or nothing if no output was
                        generated"""

    r: str = ""

    async with aiohttp.ClientSession(**(session_args or {})) as session:
        async with session.post(
            url=api,
            json={
                "streamResponse": True,
                "forceNoEnd": no_end,
                "keywords": keywords or [],
                "length": length,
                "prompt": {
                    "text": prompt,
                    "isContinuation": continuation,
                },
                "startFromBeginning": begining,
                "temperature": temperature,
                "topP": probability,
            },
            **(request_args or {})
        ) as response:
            async for line in response.content:
                r += json.loads(line.decode())["data"]["text"]

    return r
