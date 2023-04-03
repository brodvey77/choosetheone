from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)

API_TOKEN: str = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Собак 🦮')
button_2: KeyboardButton = KeyboardButton(text='Огурцов 🥒')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_1, button_2]],
                                    resize_keyboard=True)

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Чего кошки боятся больше?', reply_markup=keyboard)


# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
@dp.message(Text(text='Собак 🦮'))
async def process_dog_answer(message: Message):
    await message.answer(text='Да, несомненно, кошки бояться собак. '
                              'Но вы видели как они бояться огурцов?', reply_markup=ReplyKeyboardRemove())


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
@dp.message(Text(text='Огурцов 🥒'))
async def process_cucumber_answer(message: Message):
    await message.answer(text='Да, иногда кажется, что огурцов '
                              'кошки бояться больше',
                         reply_markup=ReplyKeyboardRemove())


if __name__ == "__main__":
    dp.run_polling(bot)

