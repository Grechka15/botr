from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.routes6 import router, notifier
from aiogram.client.default import DefaultBotProperties
import aiohttp
from aiogram.client.session.aiohttp import AiohttpSession
from aiohttp import ClientTimeout


session = AiohttpSession(
    timeout=ClientTimeout(
        total=60,             # Максимальное время на весь запрос
        connect=10,          # Время на установку соединения
        sock_read=10,        # Время на чтение данных из сокета
        sock_connect=10
        )
)

load_dotenv()


TOKEN = getenv("BOT_TOKEN")

#Объект
dp = Dispatcher()

dp.include_router(router)


# Передаем сессию в конструктор Bot
async def main():
    session = AiohttpSession()
    
    bot = Bot(
        token=TOKEN, 
        session=session,
        default=DefaultBotProperties(parse_mode="HTML")
    )

    asyncio.create_task(notifier(bot))

    print("Start")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

