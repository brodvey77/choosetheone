from environs import Env


env = Env()         # Создаем экземпляр класса ENV
env.read_env()      # Методом read_env() читаем файл .env
                    # и загружаем из него переменные в окружение


bot_token = env('BOT_TOKEN')         # Сохраняем значение переменной окружения в переменную bot_token
admin_id = env.int('ADMIN_ID')       # Преобразуем значение переменной окружения к типу int
                                     # и сохраняем в переменной admin_id


print(bot_token)
print(admin_id)