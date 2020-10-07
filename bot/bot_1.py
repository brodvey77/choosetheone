import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)

bot = Bot(token='1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4')
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton(text='создать викторину',
                                           request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
    poll_keyboard.add(types.KeyboardButton(text='Отмена'))
    await message.answer("Нажмите на кнопку ниже и создайте викторину!", reply_markup=poll_keyboard)

@dp.message_handler(lambda message: message.text == "Отмена")
async def action_cancel(message: types.Message):
    remove_keyboard = types.ReplyKeyboardRemove()
    await message.answer("Действие отменено. Введите /start, чтобы начать заново.", reply_markup=remove_keyboard)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


