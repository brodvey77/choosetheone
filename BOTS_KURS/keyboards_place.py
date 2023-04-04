from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)

API_TOKEN: str = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

buttons: list[KeyboardButton] = []
keyboard: list[list[KeyboardButton]] = []

# Заполняем список списками с кнопками
for i in range(1, 1201):
    buttons.append(KeyboardButton(text=str(i)))
    if not i % 12:
        keyboard.append(buttons)
        buttons = []

# Создаем объект клавиатуры, добавляя в него список списков с кнопками
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                        keyboard=keyboard,
                                        resize_keyboard=True)

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это тест кнопок', reply_markup=my_keyboard)





if __name__ == "__main__":
    dp.run_polling(bot)