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