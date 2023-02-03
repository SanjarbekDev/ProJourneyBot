import os
import openai
from data.config import OPENAI_API_KEY
from typing import Union

openai.organization = "org-LWOO4CuRHW3aJ4X7oGEcZ0rT"

async def imagenie(prompt : str , size : str):
    openai.api_key = OPENAI_API_KEY
    image = openai.Image.create(
      prompt=prompt,
      n=2,
      size=size
    )
    return image

async def Create_variant(file_path):
    openai.api_key = OPENAI_API_KEY
    dirs = file_path
    with open(dirs , "rb") as image:
        variant = openai.Image.create_variation(
            image = image,
            n = 1 
        )

    return variant





