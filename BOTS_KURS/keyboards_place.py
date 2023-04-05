from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text, Command
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo




API_TOKEN: str = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем список списков с кнопками
keyboard: list[list[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]]

keyboard.append([KeyboardButton(text='7')])

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='test 6', reply_markup=my_keyboard)

# # Создаем кнопку
# web_app_btn: KeyboardButton = KeyboardButton(text='Start Web App', web_app=WebAppInfo(url="https://you.com/"))
#
# # Создаем объект клавиатуры
# web_app_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[web_app_btn]], resize_keyboard=True)
#
#
# # Этот хэндлер будет срабатывать на команду "/web_app"
# @dp.message(Command(commands='web_app'))
# async def process_web_app_command(message: Message):
#     await message.answer(text='Экспериментируем со специальными кнопками', reply_markup=web_app_keyboard)

# poll_btn: KeyboardButton = KeyboardButton(text='Create poll', request_poll=KeyboardButtonPollType(type='regular'))
#
# quiz_btn: KeyboardButton = KeyboardButton(text='Start quiz', request_poll=KeyboardButtonPollType(type='quiz)'))
#
#
# kb_builder.row(poll_btn, quiz_btn, width=1)
#
# keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True)
#
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text='This is special buttons', reply_markup=keyboard)

# Создаем кнопки
# btn_1: KeyboardButton = KeyboardButton(text='Кнопка 1')
# btn_2: KeyboardButton = KeyboardButton(text='Кнопка 2')
#
# # Создаем объект клавиатуры
# placeholder_exmpl_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
#                                     keyboard=[[btn_1, btn_2]],
#                                     resize_keyboard=True,
#                                     input_field_placeholder='fuck you')
#
#
# # Этот хэндлер будет срабатывать на команду "/placeholder"
# @dp.message(Command(commands='placeholder'))
# async def process_placeholder_command(message: Message):
#     await message.answer(text='Экспериментируем с полем placeholder',
#                          reply_markup=placeholder_exmpl_kb)

if __name__ == "__main__":
    dp.run_polling(bot)