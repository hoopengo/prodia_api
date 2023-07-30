#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prodia image generation api"""

import random
import time
import typing

import requests

from .. import const, enums


def prodia(
    prompt: str,
    model: enums.ProdiaModel = enums.ProdiaModel.REALISTIC_VISION_V5_0,
    steps: int = const.DEFAULT_PRODIA_STEPS,
    cfg: float = const.DEFAULT_PRODIA_CFG,
    seed: int = -1,
    sampler: enums.ProdiaSampler = enums.ProdiaSampler.EULER,
    negative: bool = True,
    negative_prompt: str = const.DEFAULT_PRODIA_NEG,
    image: bool = True,
    sleep: float = const.DEFAULT_PRODIA_SLEEP,
    api: str = const.DEFAULT_PRODIA_API,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
    session_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> bytes:
    """prodia image api ( proxies dont work + limited uses )

    *prompt(str): the prompt passed to the ai
    model(..enums.ProdiaModel): the prodia model to use to generate images
    steps(int): generation steps
    cfg(float): how strongly the image should conform to the text
    seed(int): seed to use to generate image ( <0 = random )
    sampler(..enums.ProdiaSampler): algorithm to use to generate the image
    negative(bool): enable / disable negative output filtering
    negative_prompt(str): filter / profile for the negative output
    image(bool): if set to true returns the image as bytes, if not returns the
                 url encoded in bytes ( use `str.decode()` to decode it )
    sleep(float): how much time to sleep between every ping request to the job
    api(str): api url for the alpaca model
    request_args(dict[str, Any] | None): arguments passed to `requests.get()`

    return(bytes): jpeg image as bytes if `image` is `True` else image url
                   encoded in utf-8"""

    request_args = request_args or {}
    session: requests.Session = requests.Session(**(session_args or {}))

    job_id: str = session.get(
        f"{api}/generate",
        params={
            "new": "true",
            "prompt": prompt,
            "model": model.value,
            "negative_prompt": negative_prompt if negative else "",
            "steps": steps,
            "cfg": cfg,
            "seed": random.randint(0, 9999999999999) if seed < 0 else seed,
            "sampler": sampler.value,
            "aspect_ratio": "square",
        },
        **request_args,
    ).json()["job"]

    while True:
        if (
            session.get(
                f"{api}/job/{job_id}",
                **request_args,
            ).json()["status"]
            == "succeeded"
        ):
            url: str = f"https://images.prodia.xyz/{job_id}.png?download=1"
            return (
                session.get(
                    url,
                    **request_args,
                ).content
                if image
                else url.encode()
            )

        time.sleep(sleep)
