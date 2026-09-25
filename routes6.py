#Подписки и уведомления
#------------
#------------
#------------

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
import aiohttp
from aiogram import Bot
import aiosqlite
import asyncio

router = Router()


subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user_id in list(subscribers):
                try:
                    await bot.send_message(user_id, "Сообщение")
                except Exception:
                    pass
        await asyncio.sleep(10)


@router.message(Command("start"))
async def start (message: Message):
    await message.answer(
        "Привет!\n"
        "Я могу помочь с рассылкой\n\n"
        "Команды:\n"
        "/subscribe - "
        "/unsubscribe - "
        "/subscribers - "        
    )
@router.message(Command("subscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id

    subscribers.add(user_id)
    await message.answer("Вы подписаны")

@router.message(Command("unsubscribe"))
async def unsubscribe(message: Message):
    user_id = message.from_user.id

    subscribers.discard(user_id)
    await message.answer("Вы отписались")

@router.message(Command("subscribers"))
async def subscribers_cmd(message: Message):
    if not subscribers:
        await message.answer("Никого нет")
        return
    text = "Подписчики:\n"
    for uid in subscribers:
        text += f"{uid}\n"
    await message.answer(text)



