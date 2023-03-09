# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command
# from aiogram.types import Message
# import logging
#
# # Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
# API_TOKEN: str = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'
#
# # Создаем объекты бота и диспетчера
# bot: Bot = Bot(token=API_TOKEN)
# dp: Dispatcher = Dispatcher()
#
# # Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Этот хэндлер будет срабатывать на команду "/start"
# @dp.message(Command(commands=['start']))
# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот\nНапиши мне что-нибудь')
#
#
# # Этот хэндлер будет срабатывать на команду "/help"
# @dp.message(Command(commands=['help']))
# async def process_help_command(message: Message):
#     await message.answer('Напиши мне что-нибудь и в ответ'    #await bot.send_message(message.chat.id, message.text)
#                          'я пришлю тебе твоё сообщение')
#
#
# # Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# # кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)
#
# if __name__ == '__main__':
#     dp.run_polling(bot)




#Регистрация хэндлеров в диспетчере

# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import Command
# from aiogram.types import Message, ContentType
# import logging
#
#
# API_TOKEN = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'
#
# #Configure logging
# logging.basicConfig(level=logging.INFO)
#
# bot: Bot = Bot(token=API_TOKEN)
# dp: Dispatcher = Dispatcher()
#
# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
#
#
# async def process_help_command(message: Message):
#     await message.answer('Напиши мне что-нибудь и в ответ '
#                          'я пришлю тебе твое сообщение')
#
#
# # Этот хэндлер будет срабатывать на отправку боту фото
# async def send_photo_echo(message: Message):
#     await message.reply_photo(message.photo[0].file_id)
#
#
# async def send_sticker_echo(message: Message):
#     await message.reply_sticker(message.sticker.file_id)
#
#
# async def send_echo(message: Message):
#     await message.reply(text=message.text)
#
# # Регистрируем хэндлеры
# dp.message.register(process_start_command, Command(commands=['start']))
# dp.message.register(process_help_command, Command(commands='help'))
# dp.message.register(send_photo_echo, F.photo)
# dp.message.register(send_sticker_echo, F.sticker)
# dp.message.register(send_echo)
#
# if __name__ == '__main__':
#     dp.run_polling(bot)


#
# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command
# from aiogram.types import Message
# import logging
#
#
# API_TOKEN: str = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'
#
# # #Configure logging
# logging.basicConfig(level=logging.INFO)
#
# # Создаем объекты бота и диспетчера
# bot: Bot = Bot(token=API_TOKEN)
# dp: Dispatcher = Dispatcher()
#
# # Этот хэндлер будет срабатывать на команду "/start"
# @dp.message(Command(commands=['start']))
# async def process_start_command(message: Message):
#     await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')
#
#
# # Этот хэндлер будет срабатывать на команду "/help"
# @dp.message(Command(commands=['help']))
# async def process_help_command(message: Message):
#     await message.answer('Напиши мне что-нибудь и в ответ '
#                          'я пришлю тебе твое сообщение')
#
#
#
# # Этот хэндлер будет срабатывать на любые ваши сообщения,
# # кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text='Данный тип апдейтов не поддерживается '
#                                  'методом send_copy')
#
# if __name__ == '__main__':
#     dp.run_polling(bot)


