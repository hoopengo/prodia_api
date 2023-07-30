#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""enums of models and whatnot"""

from enum import Enum


class ProdiaModel(Enum):
    """prodia image generation models"""

    ANALOG_V1 = "analog-diffusion-1.0.ckpt [9ca13f02]"
    ANYTHING_V3 = "anythingv3_0-pruned.ckpt [2700c435]"
    ANYTHING_V4_5 = "anything-v4.5-pruned.ckpt [65745d25]"
    ANYTHING_V5 = "anythingV5_PrtRE.safetensors [893e49b9]"
    ABYSSORANGEMIX_V3 = "AOM3A3_orangemixs.safetensors [9600da17]"
    DELIBERATE_V2 = "deliberate_v2.safetensors [10ec4b29]"
    DREAMLIKE_DIFFUSION_V1 = "dreamlike-diffusion-1.0.safetensors [5c9fd6e0]"
    DREAMLIKE_DIFFUSION_V2 = "dreamlike-diffusion-2.0.safetensors [fdcf65e7]"
    DREAMSHAPER_5_BAKED_VAE = "dreamshaper_5BakedVae.safetensors [a3fbf318]"
    DREAMSHAPER_6_BAKED_VAE = "dreamshaper_6BakedVae.safetensors [114c8abb]"
    DREAMSHAPER_7 = "dreamshaper_7.safetensors [5cf5ae06]"
    EIMIS_ANIME_DIFFUSION_V1_0 = "EimisAnimeDiffusion_V1.ckpt [4f828a15]"
    ELLDRETH_VIVID = "elldreths-vivid-mix.safetensors [342d9d26]"
    LYRIEL_V1_5 = "lyriel_v15.safetensors [65d547c5]"
    LYRIEL_V1_6 = "lyriel_v16.safetensors [68fceea2]"
    MECHAMIX_V1_0 = "mechamix_v10.safetensors [ee685731]"
    MEINAMIX_MEINA_V9 = "meinamix_meinaV9.safetensors [2ec66ab0]"
    MEINAMIX_MEINA_V11 = "meinamix_meinaV11.safetensors [b56ce717]"
    OPENJOURNEY_V4 = "openjourney_V4.ckpt [ca2f377f]"
    PORTRAIT_PLUS_V1 = "portraitplus_V1.0.safetensors [1400e684]"
    REALISTIC_VISION_V1_4 = "Realistic_Vision_V1.4-pruned-fp16.safetensors [8d21810b]"
    REALISTIC_VISION_V2_0 = "Realistic_Vision_V2.0.safetensors [79587710]"
    REALISTIC_VISION_V4_0 = "Realistic_Vision_V4.0.safetensors [29a7afaa]"
    REALISTIC_VISION_V5_0 = "Realistic_Vision_V5.0.safetensors [614d1063]"
    REDSHIFT_DIFFUSION_V1_0 = "redshift_diffusion-V10.safetensors [1400e684]"
    REV_ANIMATED_V1_2_2 = "revAnimated_v122.safetensors [3f4fefd9]"
    SD_V1_4 = "sdv1_4.ckpt [7460a6fa]"
    SD_V1_5 = "v1-5-pruned-emaonly.ckpt [81761151]"
    SHONIN_BEAUTIFUL_PEOPLE_V1_0 = "shoninsBeautiful_v10.safetensors [25d8c546]"
    THEALLY_MIX_II = "theallys-mix-ii-churned.safetensors [5d9225a4]"
    TIMELESS_V1 = "timeless-1.0.ckpt [7c4971d4]"


class ProdiaSampler(Enum):
    """prodia image generation samplers"""

    EULER = "Euler"
    EULER_A = "Euler a"
    HEUN = "Heun"
    DPMPP_2M_KARRAS = "DPM++ 2M Karras"
    DPMPP_SDE_KARRAS = "DPM++ SDE Karras"
    DDIM = "DDIM"


class DeepAIModel(Enum):
    """deepai models enum"""

    TEXT2IMG = "text2img"
    IMAGE_EDITOR = "image-editor"
    TEXT = "text-generator"
    FANTASY_WORLD = "fantasy-world-generator"
    UPSCALE = "torch-srgan"
    STABLE_DIFFUSION = "stable-diffusion"
    WAIFU2X = "waifu2x"
    NSFW_DETECTOR = "nsfw-detector"
    CYBERPUNK = "cuberpunk-generator"
    IMAGE_SIMILARITY = "image-similarity"
    CUTE_CREATURE = "cute-creature-generator"
    RENAISSANCE_PAINTING = "renaissance-painting-generator"
    OLD_DRAWING = "old-style-generator"
    ANIME_PORTRAIT = "anime-portrait-generator"
    SURREAL_GRAPHICS = "surreal-graphics-generator"
    OBJECTS_3D = "3d-objects-generator"
    IMPRESSIONISM_PAINTING = "impressionism-painting-generator"
    WATERCOLOR_PAINTING = "watercolor-painting-generator"
    CHARACTER_3D = "3d-character-generator"
    FUTURE_ARCHITECTURE = "future-architecture-generator"
    ANIME_WORLD = "anime-world-generator"
    STEAMPUNK = "steampunk_generator"
    STREET_ART = "street-art-generator"
    ORIGAMI_3D = "origami-3d-generator"
    HOLOGRAM_3D = "hologram-3d-generator"
