# coding=utf-8
height = input('Введите высоту: ')
h = int(height)

while 0 == 0:
    if h > 0 and h <= 23:
        for i in range(h):
            print(' ' * (h - i - 1) + '#' * (i + 2))
        break
    elif h < 1:
        h = int(input('Высота не может быть равной нулю и отрицательной. Введите другую: '))
    elif h > 23:
        h = int(input('Высота слишком большая. Введите высоту поменьше: '))


