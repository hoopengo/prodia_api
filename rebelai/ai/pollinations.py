#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pollinations image ai"""

import random
import typing

import requests

from .. import const


def pollinations(
    prompt: str,
    api: str = const.DEFAULT_POLLINATIONS_API,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> bytes:
    """pollinations api access ( proxies suggested + watermark )

    *prompt(str): the prompt passed to the ai
    api(str): api url for the alpaca model
    request_args(dict[str, Any] | None): arguments passed to `requests.get()`

    return(bytes): jpeg image as bytes"""

    return requests.get(
        f"{api}/{prompt}{random.randint(0, 9999999999999)}",
        **(request_args or {}),
    ).content
