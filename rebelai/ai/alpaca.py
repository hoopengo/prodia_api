#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""alpaca models"""

import typing

import requests

from .. import const


def alpaca_7b(
    prompt: str,
    api: str = const.DEFAULT_ALPACA_7B_API,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> typing.Optional[str]:
    """alpaca ( 7 bilion neuron ) access

    *prompt(str): the prompt passed to the ai
    api(str): api url for the alpaca model
    request_args(dict[str, Any] | None): arguments passed to `requests.post()`

    return(str | None): the ai output as a string or nothing if no output was
                        generated"""

    return (
        requests.post(
            api,
            json={"prompt": prompt},
            **(request_args or {}),
        )
        .json()
        .get("completion")
    )
