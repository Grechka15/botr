#РАБОТА С КОМАНДАМИ
#------------------
#------------------

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Я_Серега")],
            [KeyboardButton(trxt="Я_не_Серега")][KeyboardButton(text='Старт')]
        ],
        resize_keyboard=True
    )
    return keyboard

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        f"Сергей Петух\n *петушок*\n\n _нaпиши_ /help",
        parse_mode="Markdown")

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Список команд:\n\n/about информация про сергея")

@router.message(Command("about"))
async def about(message: Message):
    await message.answer(
        f"Сергей - Гей, ты :{message.from_user.first_name}\n\n <a href='https://google.com'> ссылка </a>",
        parse_mode="HTML",
        reply_markup=get_main_reply_keyboard())

@router.message()
async def start(message: Message):
    await message.answer("Лох")