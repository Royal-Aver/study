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
a = "+7(912)123-45-67"
lst = list(a)
for el in lst:
    if el == '+' or el == '-':
        lst.remove(el)
    elif el == '7':
        lst.remove(el)
lst.insert(0, '8')

print("".join(lst))
