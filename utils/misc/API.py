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



