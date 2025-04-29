"""
Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
number — натуральное число
Функция должна выводить все цифры числа number, начиная с младших разрядов, каждое на отдельной строке.
"""


def print_digits(number):
    if number > 0:
        print(number % 10)
        print_digits(number // 10)


print_digits(12345)
