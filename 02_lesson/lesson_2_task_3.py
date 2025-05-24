# площадь квадрата S = a × a = a²

import math

side_square = float(input("Введите длину стороны квадрата: "))


def calculate_square_area(side):
    area = side * side
    print(math.ceil(area))


calculate_square_area(side_square)
