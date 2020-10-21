# from aiogram import Bot
# from aiogram.utils import executor
# bot = Bot(token='1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4')


# executor.start_polling()

import logging
from aiogram import Bot, Dispatcher, executor, types
from curs import func_cource_of_euro

API_TOKEN = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('D:/1.jpeg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')


@dp.message_handler(commands=['euro'])
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    
    await message.answer(func_cource_of_euro())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
