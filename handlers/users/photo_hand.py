from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, bot
from utils.misc.API import Create_variant
from pathlib import Path
from PIL import Image
from io import BytesIO
import os
import openai

#fayllar uchun catalog yaratamiz
download_path=Path().joinpath('Downloads','categories')
download_path.mkdir(parents=True,exist_ok=True)

@dp.message_handler(content_types='photo')
async def create_v(msg : types.Message):

    try:
        file = await msg.photo[-1].get_file()
        if file['file_size'] > 400000:
            return await msg.reply('Rasim hajmi katta, iltimos kichikroq rasim yuboring!')
        await file.download(destination_dir = download_path)
        file_path = f"{download_path}/{file['file_path']}"
        img = Image.open(file_path)
        width, height = 256, 256
        img = img.resize((width, height))

        byte_stream = BytesIO()
        img.save(byte_stream, format='PNG')
        byte_array = byte_stream.getvalue()

        response = openai.Image.create_variation(
                image=byte_array,
                n=1,
                size="1024x1024"
            )

        os.remove(file_path)
        print(response)
        await msg.reply_photo(photo=response['data'][0]['url'], caption=f"#var{response['created']}" )      
    except:
        await msg.reply("<b>Xato ! \nQayta urunib ko'ring</b>")

