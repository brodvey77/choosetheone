# -*- coding: utf-8 -*-

# pip install simple_draw

import simple_draw as sd

# нарисовать треугольник из точки (300, 300) с длиной стороны 200
# length = 200
# point = sd.get_point(200, 200)
#
# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=5,)
# v1.draw()
# v2 = sd.get_vector(start_point=v1.end_point,angle=90, length=200, width=5)
# v2.draw()
# v3 = sd.get_vector(start_point=v2.end_point,angle=180, length=200, width=5)
# v3.draw()
# v4 = sd.get_vector(start_point=v3.end_point, angle=270, length=200, width=5)
# v4.draw()

#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=250, width=3)
# v2.draw()
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=250, width=3)
# v3.draw()

# v1 = sd.get_vector(start_point=point, angle=0, length=200, width=3)
# v1.draw()
#
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=200, width=3)
# v2.draw()
#
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=200, width=3)
# v3.draw()

# определить функцию рисования треугольника из заданной точки с заданным наклоном
#

# def draw_tringle(point, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=5)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle= angle + 90, length=200, width=5)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle = angle + 180, length=200, width=5)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle = angle + 270, length=200, width=5)
#     v4.draw()
#
# point_0 = sd.get_point(300, 300)
# for angle in range(0, 361, 30):
#     draw_tringle(point=point_0, angle=angle)

# def draw_tringle(point, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=250, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=250, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=250, width=3)
#     v3.draw()
#
# point_0 = sd.get_point(300, 300)
#
# for angle in range(0, 361, 30):
#     draw_tringle(point=point_0, angle=angle)

# def triangle(point, angle=0):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=200, width=3)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=200, width=3)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=200, width=3)
#     v3.draw()
#
#
# point_0 = sd.get_point(300, 300)
#
# for angle in range(0, 361, 30):
#     triangle(point=point_0, angle=angle)

# 2142
point_0 = sd.get_point(300, 5)

# v1 = sd.get_vector(start_point=point_0, angle=90,length=100)
# v1.draw()
# def branch(point, angle, lenght):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
#     v1.draw()
#     return v1.end_point

# angle_0 = 90
# leight_0 = 100
# next_point = branch(point=point_0, angle=angle_0, lenght=leight_0)
# next_angle = angle_0 - 30
# next_leight = leight_0 * .75
# next_point = branch(point=next_point, angle=next_angle, lenght=next_leight * 0.75)
# next_angle = next_angle - 30
# next_leight = leight_0 * .75
# next_point = branch(point=next_point, angle=next_angle, lenght=next_leight * 0.75)
# next_angle = next_angle - 30
# next_leight = leight_0 * .75
# next_point = branch(point=next_point, angle=next_angle, lenght=next_leight * 0.75)
# next_angle = next_angle - 30
# next_leight = leight_0 * .75
# next_point = branch(point=next_point, angle=next_angle, lenght=next_leight * 0.75)



# angle_0 = 90
# leight_0 = 100
# next_angle = angle_0
# next_leight = leight_0
# next_point = point_0
#
# while next_leight > 1:
#     next_point = branch(point=next_point, angle=next_angle, lenght=next_leight)
#     next_angle = next_angle - 30
#     next_leight = next_leight * .75


def branch(point, angle, lenght, delta):
    if lenght < 1:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=lenght, width=3)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_lenght = lenght * .75
    branch(point=next_point, angle=next_angle, lenght=next_lenght, delta=delta)

# for lenght in range(50, 200, 5):
#     branch(point=point_0, angle=90, lenght=200, delta=30)

for delta in range(0, 51, 10):
    branch(point=point_0, angle=90, lenght=150, delta=delta)
for delta in range(-50, 1, 10):
    branch(point=point_0, angle=90, lenght=150, delta=delta)
# branch(point=point_0, angle=90, lenght=100, delta=50)
# branch(point=point_0, angle=90, lenght=150, delta=60)



sd.pause()

