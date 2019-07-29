# Курс основы программирования на Python
# Задание по программированию: Больше предыдущего
# 09.05.2019
#
# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
#
# Формат ввода
#
# Вводится список чисел. Все числа списка находятся на одной строке.
#
# Формат вывода
#
# Выведите ответ на задачу.

numList = list(map(int, input().split()))
maximum = []
for i in range(len(numList)):
    if i >= 1:
        if numList[i] > numList[i - 1]:
            maximum.append(numList[i])

print(' '.join(map(str, maximum)))
