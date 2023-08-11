#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""deepL translation api"""

import json
import random
import time
import typing

import aiohttp

from .. import const


async def deepl(
    prompt: str,
    source_lang: str,
    target_lang: str,
    alternatives: int = 0,
    api: str = const.DEFAULT_DEEPL_API,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
    session_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> typing.Optional[typing.Tuple[str, ...]]:
    """deepL AI translation

    *prompt(str): the prompt passed to the ai
    *source_lang(str): the language of the source, format : language code in uppercase
    *target_lang(str): the language you want to translate the source to, same format
    alternatives(int): the count of alternatives you want, max is 3
    api(str): api url for the deepl model
    request_args(dict[str, Any] | None): arguments passed to `session.post()`
    session_args(dict[str, Any] | None): arguments passed to `aiohttp.ClientSession()`

    return(tuple[str, ...] | None): the translations, `None` if no results are
                                    returned"""

    ts: int = int((t := time.time()) * 1000)

    if (ic := prompt.count("i")) != 0:
        ic += 1
        ts = ts - ts % ic + ic

    random.seed(t)
    tid: int = random.randint(8300000, 8399998) * 1000

    d: str = json.dumps(
        {
            "jsonrpc": "2.0",
            "method": "LMT_handle_texts",
            "id": tid,
            "params": {
                "texts": [{"text": prompt, "requestAlternatives": alternatives}],
                "splitting": "newlines",
                "lang": {
                    "source_lang_user_selected": source_lang,
                    "target_lang": target_lang,
                },
                "timestamp": ts,
                "commonJobParams": {
                    "wasSpoken": False,
                    "transcribe_as": "",
                },
            },
        },
        ensure_ascii=False,
    ).replace(
        '"method":"',
        f'"method"{" " if (tid + 5) % 29 == 0 or (tid + 3) % 13 == 0 else ""}: "',
        -1,
    )

    async with aiohttp.ClientSession(**(session_args or {})) as session:
        async with session.post(
            url=api,
            data=d,
            headers={
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip, deflate, br",
            },  # this is why we need `brotli` as a dependency
            **(request_args or {}),
        ) as response:
            texts: typing.Dict[str, typing.Any] = await response.json()

            if "result" not in texts:
                return None

            texts = texts["result"]["texts"][0]

            return (texts["text"],) + tuple(
                alt["text"] for alt in texts["alternatives"]
            )
