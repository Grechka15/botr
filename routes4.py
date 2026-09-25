#API: РАБОТА С САЙТАМ
#------------------
#------------------

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery, 
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from handlers.user1 import Form
from aiogram import Bot
from aiogram.types import FSInputFile


router = Router()

# --------
# --------

import aiohttp

async def  get_product(product_id):
    url = f"https://fakestoreapi.com/products/{product_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 404:
                return None
            data = await resp.json()
            return data
        
# --------    
# --------


@router.message(Command("start"))
async def start (message: Message):
    await message.answer("Здарова, заебал\nПиши ID прродукта\n\nНапример: /product 1")



@router.message(Command("product"))
async def get_product_cmd(message: Message):
    parts = message.text.strip().split()

    if len(parts) != 2:
        await message.answer("Используйте: product 1")
        return

    product_id = parts[1]
    if not product_id.isdigit():
        await message.answer("Числом")
        return

    await message.answer(f"Ищу товар с id: {product_id}")

    try:
        product = await get_product(int(product_id))
    except Exception:
        await message.answer("Не удалось обратиться, рядовой")
        return

    if product is None:
        await message.answer("Такого товара нет")
        return

    title = product.get("title", "Без названия")
    price = product.get("price", "-")
    desc = product.get("description", "Без названия")
    category = product.get("category", "Без названия")

    text = (
        f"<b>{title}</b>\n\n"
        f"Категория: <i>{category}</i>\n"
        f"Цена: <b>{price}$</b>\n"
        f"{desc}"
    )
    await message.answer(text, parse_mode="HTML")

    # ------

#   image = product.get("image")
#   if image:
#       await message.answer_photo(photo=image, caption=text, parse_mode="HTML")
#   else:
#       await message.answer(text, pawse_mode="HTML")

    # ------

    
        


   

                        


 
