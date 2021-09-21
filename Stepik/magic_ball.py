# project Magic Ball

# import random
# import time
#
# answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай", "Предрешено",
#            "Вероятнее всего", "Спроси позже", "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы",
#            "Лучше не рассказывать", "По моим данным - нет", "Можешь быть уверен в этом", "Да",
#            "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
#
# print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
# time.sleep(1)
# user_name = input('Как Вас зовут? ')
# time.sleep(1)
# print(f'Привет {user_name}')
#
#
# def input_data():
#     while True:
#         question = input(f'{user_name}, что Вас интересует? ')
#         print(random.choice(answers))
#         add_question = input(f'{user_name}, хотите ли задать еще один вопрос? д / н').lower()
#         if add_question == 'д':
#             input_data()
#         else:
#             time.sleep(0.5)
#             print('Возвращайся если возникнут вопросы!')
#             return False
#
#
# input_data()
