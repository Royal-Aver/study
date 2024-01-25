# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой равной
# n, в соответствии с примером:
# 1
# 121
# 12321
# 1234321
# 123454321
# ...

# n = 2
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for k in range(i - 1, 0, -1):
#         print(k, end='')
#     print()



# Составить программу вывода на экран вещественного числа, вводимого с клавиатуры.
# Выводимому числу должно предшествовать сообщение "Вы ввели число" (без кавычек).

# num_input = float(input('Enter your number: '))
# print(f"Вы ввели число {num_input}")


# Вводится вещественное число. Нужно проверить, что оно попадает или в диапазон [0; 2] или в диапазон [10; 20]
# (включительно). На экран вывести True, если попадает и False - в противном случае.
# Задача делается без использования условного оператора.

# float_num = 2.3
# res = (float_num >= 0 and float_num <=2) or (float_num >= 10 and float_num <=20)
# print(res)


# Вводятся два слова (через пробел в одной строке).
# Длина второго слова меньше первого. Из этих слов выделить символы с нечетными индексами с обрезкой первого
# слова до длины второго. Сравнить полученные строки между собой на равенство и результат (True или False)
# вывести на экран.
# Задачу выполнять без использования условного оператора.

# Необходимо преобразовать ее в список lst (посимвольно, то есть, элементами списка будут
# являться отдельные символы строки). Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы.
# Отобразить полученный список на экране командой:
# a, b = map(str, input().split())
# a = "+7(912)123-45-67"
# lst = list(a)
# for el in lst:
#     if el == '+' or el == '-':
#         lst.remove(el)
#     elif el == '7':
#         lst.remove(el)
# lst.insert(0, '8')
#
# print("".join(lst))

# Вводятся четыре целых числа a, b, c, d в одну строку через пробел.
# Определить, войдет ли в конверт с внутренними размерами a и b мм прямоугольная открытка с размерами с и d мм.
# Для размещения открытки в конверте необходим зазор в 1 мм с каждой стороны.
# Открытку можно поворачивать на 90 градусов.
# Вывести ДА, если входит и НЕТ - если не входит.

# a, b, c, d = map(int, input().split())
# if (c < a - 2 and d < b - 2) or (c < b - 2 and d < a - 2):
#     print('ДА')
# else:
#     print('НЕТ')


# Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число).
# По введенным m и n (в одну строку через пробел) определить:
#
# а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
# б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).
#
# В задаче принять, что год не является високосным. Вывести предыдущую дату и
# следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) в одну строчку через пробел.
#
# P.S. Число дней в месяцах не високосного года, начиная с января:
# 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

# m, n = map(int, input().split())
# if n == 1:
#     print(f"{str(m - 1).rjust(2, '0')}.31 {str(m).rjust(2, '0')}.0{n + 1}")
#
# elif int(n) == 31 or (m == 2 and n == 28) or (m == 4 or m == 6 or m == 9 or m == 11 or n == 30):
#     print(f"{str(m).rjust(2, '0')}.{int(n) - 1} {str(int(m) + 1).rjust(2, '0')}.01")
#
# else:
#     print(f"{str(m).rjust(2, '0')}.{int(n) - 1} {str(m).rjust(2, '0')}.{int(n) + 1}")


# На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных чисел,
# до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue,
# а также использовать цикл while.

# n = 1
# sum = 1
# while n != 0:
#     n = int(input())
#     if n > 0:
#         sum *= n
# print(sum)

#В виде строки записано арифметическое выражение, например:
# "10 + 25 - 12" или "10 + 25 - 12 + 20 - 1 + 3"
# и т. д. То есть, количество действий может быть разным.
# Необходимо выполнить вычисление и результат отобразить на экране.
# Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-),
# а в качестве операндов - целые неотрицательные числа.
# Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.

n = "10+25 - 12"
sum = 0
res = n.replace(' ', '').replace('+', '_+').replace('-', '_-').split('_')
for el in res:
    sum += int(el)
print(sum)
