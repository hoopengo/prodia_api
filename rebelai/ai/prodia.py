#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prodia image generation api"""

import asyncio
import random
import typing

import aiohttp

from .. import const, enums


async def prodia(
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
    """prodia image generation model access ( proxies dont work + limited uses )

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
    request_args(dict[str, Any] | None): arguments passed to `session.get()`
    session_args(dict[str, Any] | None): arguments passed to `aiohttp.ClientSession()`

    return(bytes): jpeg image as bytes if `image` is `True` else image url
                   encoded in utf-8"""

    request_args = request_args or {}

    async with aiohttp.ClientSession(**(session_args or {})) as session:
        params = {
            "new": "true",
            "prompt": prompt,
            "model": model.value,
            "negative_prompt": negative_prompt if negative else "",
            "steps": steps,
            "cfg": cfg,
            "seed": random.randint(0, 9999999999999) if seed < 0 else seed,
            "sampler": sampler.value,
            "aspect_ratio": "square",
        }

        async with session.get(
            url=f"{api}/generate",
            params=params,
            **request_args,
        ) as response:
            job_id = (await response.json())["job"]

        while True:
            async with session.get(
                url=f"{api}/job/{job_id}",
                **request_args,
            ) as response:
                status = (await response.json())["status"]

            if status == "succeeded":
                url = f"https://images.prodia.xyz/{job_id}.png?download=1"
                async with session.get(url=url, **request_args) as response:
                    return await response.read() if image else url.encode()

            await asyncio.sleep(sleep)
