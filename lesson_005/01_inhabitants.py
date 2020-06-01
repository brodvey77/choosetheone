# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import lesson_005.room_1, lesson_005.room_2

for i in lesson_005.room_1.folks:
    print("В комнате room_1 живут:" + i)
for i in lesson_005.room_2.folks:
    print("В комнате room_2 живет:" + i)


