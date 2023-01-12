import re
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from utils.misc.API import imagenie

from data.config import ADMINS
from loader import bot

@dp.message_handler(commands='imagegenerate')
async def imgsend(msg : types.Message):
    try:
        pattern = re.compile('(/imagegenerate) ?(\w\D+)? ?(\w\D+)?')
        parse_d=pattern.match(msg.text)
        prompt = parse_d.group(2)

        await msg.answer('Tez orada rasim yuboriladi iltimos kuting ...')

        img = await imagenie(prompt=prompt, size="1024x1024")
        user = msg.from_user.username
        caption = f"{user} , {prompt[:15]}..."
        await msg.answer_photo(photo=img['data'][0]['url'] , caption=caption)
        await msg.answer_photo(photo=img['data'][1]['url'] , caption=caption)

    except Exception as e:
        await bot.send_message(ADMINS[0],e)
