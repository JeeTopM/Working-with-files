"""
Реализуйте функцию triangle() с использованием рекурсии, которая принимает один аргумент:
h — натуральное число
Функция должна выводить звездный треугольник с высотой h
"""


def triangle(h):
    def rec(num):
        if num <= h:
            print("*" * num)
            rec(num + 1)

    rec(1)


# test
triangle(3)
# test
triangle(5)
