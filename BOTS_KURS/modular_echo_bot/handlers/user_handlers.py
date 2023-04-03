from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from create_dp import dp
from lexicon.lexicon import Lexicon_RU



# Этот хэндлер срабатывает на команду /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=Lexicon_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=Lexicon_RU['/help'])

