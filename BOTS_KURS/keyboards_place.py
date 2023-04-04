from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder



API_TOKEN: str = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()


buttons_1: list[KeyboardButton] = [KeyboardButton(
    text=f'button {i + 1}') for i in range(10)]

kb_builder.add(*buttons_1)
kb_builder.adjust(2, 1, repeat=True)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(text='MY KEYBOARD', reply_markup=kb_builder.as_markup(resize_keyboard=True))

if __name__ == "__main__":
    dp.run_polling(bot)