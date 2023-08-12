import asyncio
import random
import typing

import aiohttp

from . import enums

PRODIA_API = "https://api.prodia.com"


async def prodia(
    prompt: str,
    model: enums.ProdiaModel = enums.ProdiaModel.REALISTIC_VISION_V5_0,
    steps: int = 30,
    cfg: float = 7.5,
    seed: int = -1,
    sampler: enums.ProdiaSampler = enums.ProdiaSampler.EULER,
    negative: bool = True,
    negative_prompt: str = "",
    sleep: float = 1,
    request_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
    session_args: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> bytes:
    """prodia image generation model access.

    *prompt(str): the prompt passed to the ai
    model(..enums.ProdiaModel): the prodia model to use to generate images
    steps(int): generation steps
    cfg(float): how strongly the image should conform to the text
    seed(int): seed to use to generate image ( <0 = random )
    sampler(..enums.ProdiaSampler): algorithm to use to generate the image
    negative(bool): enable / disable negative output filtering
    negative_prompt(str): filter / profile for the negative output
    sleep(float): how much time to sleep between every ping request to the job
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
            url=f"{PRODIA_API}/generate",
            params=params,
            **request_args,
        ) as response:
            job_id = (await response.json())["job"]

        while True:
            async with session.get(
                url=f"{PRODIA_API}/job/{job_id}",
                **request_args,
            ) as response:
                status = (await response.json())["status"]

            if status == "succeeded":
                url = f"https://images.prodia.xyz/{job_id}.png?download=1"
                async with session.get(url=url, **request_args) as response:
                    return await response.read()

            await asyncio.sleep(sleep)
