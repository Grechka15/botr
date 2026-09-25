# РАБОТА С БАЗАМИ ДАННЫХ + ФОТО/ВИДЕО 
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

@router.message(Command("cancel"))
async def cencel_form(message: Message, state: FSMContext):
     await state.clear()
     await message.answer("Анкета отклонена")
    
@router.message(Command("start"))
async def start (message: Message, state: FSMContext):
    await message.answer("Введите ваше имя:")
    await state.set_state(Form.name)

@router.message(Form.name, F.text)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш возраст:")
    await state.set_state(Form.age)

@router.message(Form.age, F.text)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("числом пожалуйста")
        return

    if int(message.text) < 1 or int(message.text) > 100:
        await message.answer("От 1 до 100")
        return

    await state.update_data(age=int(message.text))

    await message.answer("Введите ваш почта:")
    await state.set_state(Form.email)

@router.message(Form.email, F.text)
async def process_email(message: Message, state: FSMContext):
    email_text = message.text
    if "@" not in email_text or "." not in email_text:
            await message.answer("Некорректный")
            return

    await state.update_data(email=email_text)

    data = await state.get_data()
    name = data["name"]
    age = data["age"]
    email = data["email"]
    
    await message.answer(f"Готово\nИмя: {name}\Возраст: {age}\nПочта {email} ")
    await state.set_state(Form.email)
    await state.clear()

@router.message(F.photo)
async def processes_photo(message: Message):
     photo = message.photo[-1]
     file_id = photo.file_id

     await message.answer(
          f"Вы отправили фото\n ID photo: <code>{file_id}</code>",
          parse_mode="HTML"
     )
                          

     await message.answer_photo(file_id, caption="ВОт ваше фото")

@router.message(F.document)
async def processes_document(message: Message, bot: Bot):                                         
     document = message.document
     file_id = document.file_id

     file = await bot.get_file(file_id)
     file_path = file.file_path

     local_path = f'downloads/{document.file_name}'
     await bot.download_file(file_path=file_path, destination=local_path)
     await message.answer("Файл сохранен")

@router.message(Command("file"))
async def send_file(message: Message):
     file = FSInputFile("files/example.txt")
     await message.answer_document(file)
     





