# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и
# минимальным значением дробной части элементов.

from random import randint


def rand_list(n, minn, maxx, type_numb=int, after_dot=2):
    """
    Функция для создания одномерного списка
    с псевдослучайным заполнениемю
    :param n: - длина списка
    :param minn: - минимальное число
    :param maxx: - максимальное число
    :param type_numb: - аргумент для выбора способа генерации
    :param after_dot: - количество знаков после запятой
    :return: - заполненный список
    """
    if type_numb == int:
        numbers = [randint(minn, maxx) for i in range(n)]
    elif type_numb == float:
        accuracy = 10 ** after_dot
        numbers = [(randint((minn * accuracy), (maxx * accuracy)) / accuracy) for i in range(n)]
    print('Изначальный массив: {}'.format(numbers))
    return numbers


def ost_min_max_diff(numbers):
    """
    Функция находит дробную часть от каждого число из списка
    :param numbers: - список чисел
    :return: - список дробных частей
    """
    # ost_numb = []
    # for i in range(len(numbers)):
    #     ost = round(numbers[i] * 100)
    #     hundreds = ost // 100
    #     ost -= (hundreds * 100)
    #     ost_numb.append(ost)
    ost_numb = [round(numbers[i] * 100) - ((round(numbers[i] * 100) // 100) * 100) for i in range(len(numbers))]
    return ost_numb


n = int(input('Enter length of array: '))

numbers = rand_list(n, 0, 10, float)

ost_numb = ost_min_max_diff(numbers)

diff = max(ost_numb) - min(ost_numb)
print('Min ost = {0};\nMax ost = {1};\nDifference = {2}.' \
      .format(min(ost_numb), max(ost_numb), diff))
