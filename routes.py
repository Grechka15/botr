#РАБОТА С КЛАВИШАМИ
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


router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="O боте")],
            [KeyboardButton(text="Старт"), KeyboardButton(text='Помощь')]
        ],
        resize_keyboard=True
    )
    
    return keyboard

def get_main_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть сайт", url="https://google.com")],
            [InlineKeyboardButton(text="Больше инфы", callback_data="info_more")]
        ]
    )

    return keyboard

@router.callback_query(lambda c: c.data == "info_more")
async def processes_more_info(callback):
    await callback.message.answer("Вот вся инфа")
    await callback.answer()

@router.message(Command("start"))
@router.message(F.text.lower() == "старт")
async def start(message: Message):
    await message.answer("Сергей лох",
                         reply_markup=get_main_inline_keyboard())

@router.message(Command("help"))
@router.message(F.text.lower() == "помощь")
async def start(message: Message):
    await message.answer("Серегею не помочь",
                         reply_markup=get_main_inline_keyboard())


                         
