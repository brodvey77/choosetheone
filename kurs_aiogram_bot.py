# class User:
#     def __init__(self, user_id, name, age, email):
#         self.user_id = user_id
#         self.name = name
#         self.age = age
#         self.email = email
#
# def get_user_info(user: User) -> str:
#     return f'Возраст пользователя {user.name} - {user.age}, ' \
#            f'а email - {user.email}'
#
#
# user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
# print(get_user_info(user_1))

# from dataclasses import dataclass
#
# @dataclass
# class User:
#     user_id: int
#     name: str
#     age: int
#     email: str
#
# def get_user_info(user: User) -> str:
#     return f'Возраст пользователя {user.name} - {user.age}, ' \
#            f'а email - {user.email}'
#
#
# user_1: User = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
# print(get_user_info(user_1))


# from dataclasses import dataclass
#
#
# @dataclass
# class DatabaseConfig:
#     db_host: str       # URL-адрес базы данных
#     db_user: str       # Username пользователя базы данных
#     db_password: str   # Пароль к базе данных
#     database: str      # Название базы данных
#
#
# @dataclass
# class TgBot:
#     token: str             # Токен для доступа к телеграм-боту
#     admin_ids: list[int]   # Список id администраторов бота
#
#
# @dataclass
# class Config:
#     tg_bot: TgBot
#     db: DatabaseConfig


# __annotations__
# О чем еще не сказал, так это о том, где объекты хранят аннотации типов. Для этого существует специальный атрибут __annotations__, который хранит аннотации в виде словаря с ключами - названиями переменных и значениями - их типами.
#
# Пример. Функция get_string, получающая на вход строку и число, а возвращающая строку.
#
# def get_string(string: str, number: int) -> str:
#     return string * number
# Если обратиться к атрибуту __annotations__ функции get_string:
#
# print(get_string.__annotations__)
# увидим следующий словарь:
#
# {'string': <class 'str'>, 'number': <class 'int'>, 'return': <class 'str'>}



# import requests
#
#
# api_url = 'http://api.open-notify.org/iss-now.json'
#
# response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response
#
# if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
#     print(response.text)
# else:
#     print(response.status_code)    # При другом коде ответа выводим этот код

# import requests
# api_url = 'http://numbersapi.com/43'
#
# response = requests.get(api_url)
#
# if response.status_code == 200:
#     print(response.text)
# else:
#     print(response.status_code)




# def custom_filter(l: list):
#     flag = False
#     l = list(filter(lambda x: type(x) == int, l))
#     l = list(filter(lambda x: x%7 == 0, l))
#     if sum(l) < 83:
#         flag = True
#     return flag
#
#
#
# some_list = [7, 14, 28, 32, 32, 56]
#
# print(custom_filter(some_list))

# class MyClass:
#     def __int__(self)->None:
#         pass
#
# my_class_1 = MyClass()
# my_class_2 = MyClass()
#
# print(my_class_1)
# print(my_class_2)
#
# print(my_class_1())

# class MyClass:
#     def __int__(self) -> None:
#         pass
#
#     def __call__(self) -> str:
#         return 'результат вызова экземпляра класса'
#
# my_class_1 = MyClass()
# my_class_2 = MyClass()
# print(my_class_1())
# print(my_class_2())


# from aiogram.filters import BaseFilter
#
# admin_ids: list[int] = [173901673, 178876776, 197177271]
#
# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         self.admin_ids = admin_ids
#
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids


# class IsAdmin(BaseFilter):
#     admins: str
#
#     async def __call__(self, message: Message) -> bool:
#         return str(message.chat.id) == admins

# from aiogram import Bot, Dispatcher
# from aiogram.filters import BaseFilter, Command
# from aiogram.types import Message
# import logging
#
# logging.basicConfig(level=logging.INFO)
#
# API_TOKEN: str = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'
#
# # Создаем объекты бота
# bot: Bot = Bot(token=API_TOKEN)
# dp: Dispatcher = Dispatcher()
#
# # Список с ID администраторов бота.
# admin_ids: list[int] = [237071938]


# @dp.message(Command(commands=['start']))
# async def start_command(message: Message):
#     await message.answer(text=f'{message.from_user.id}')


# Собственный фильтр, проверяющий юзера на админа
# class IsAdmin(BaseFilter):
#     def __init__(self, admin_ids: list[int]) -> None:
#         # В качестве параметра фильтр принимает список с целыми числами
#         self.admin_ids = admin_ids
#
#     async def __call__(self, message: Message) -> bool:
#         return message.from_user.id in self.admin_ids
#
#
#
# @dp.message(IsAdmin(admin_ids))
# async def answer_if_admins_update(message: Message):
#     await message.answer(text='You are Admin')
#
#
#
# @dp.message()
# async def answer_if_not_admins_update(message: Message):
#     await message.answer(text='You are not admin')
#
#
# if __name__ == "__main__":
#     dp.run_polling(bot)

from aiogram import Bot, Dispatcher
from aiogram.filters import BaseFilter, Text
from aiogram. types import Message
import logging

API_TOKEN: str = '1363273986:AAEHIpzsNhJYEeeiN1I3s4sAr4j86vQYVL4'
logging.basicConfig(level=logging.INFO)

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Это фильтр будет проверять наличие неотрецательных чисел
# в сообщении от пользователя и передавать в хэндлер их список
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимыесимволы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам и добавляем их в список
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(normalized_word)
        # Если в списке есть числа - возвращаем список по ключу 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False


# Этот хэндлер будет срабатывать если сообщениепользователя
# начинается с фразы "Найди числа".
@dp.message(Text(startswith='найди числа', ignore_case=True), NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список из фильтра
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
        text=f'Нашёл: {str(", ".join(str(num) for num in numbers))}')


# Этот хэндлер будет срабатывать если сообщение пользователя
# начинается с фразы "Найди числа, но в нем нет чисел
@dp.message(Text(startswith='найди числа', ignore_case=True))
async def process_if_not_numbers(message: Message):
    await message.answer(
        text='Не нашёл почему-то :('
    )


if __name__ == "__main__":
    dp.run_polling(bot)









