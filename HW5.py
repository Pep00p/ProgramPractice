# Вариант 2
# a) Объединение словарей с суммированием значений: Даны два словаря. Если ключи совпадают, их значения нужно сложить.
# Ввод	Вывод
# {'a': 10, 'b': 20}, {'b': 5, 'c': 15}	{'a': 10, 'b': 25, 'c': 15}

# б) Частота элементов в кортеже: Дан кортеж чисел. Нужно вернуть словарь с частотой каждого числа.
# Ввод	Вывод
# (1, 2, 2, 3, 3, 3)	{1: 1, 2: 2, 3: 3}

# c) Поиск самого длинного ключа в словаре: Дан словарь с строковыми ключами. Найти ключ с наибольшей длиной.
# Ввод	Вывод
# {'apple': 5, 'banana': 3, 'watermelon': 7}	'watermelon'

# d) Перемешивание кортежа: Дан кортеж. Нужно случайным образом перемешать его элементы.
# Ввод	Вывод
# (1, 2, 3, 4, 5)	(например) (3, 1, 5, 2, 4)

# e) Разбиение словаря на кортежи: Дан словарь. Преобразовать его в список кортежей (ключ, значение).
# Ввод	Вывод
# {'x': 10, 'y': 20, 'z': 30}	[('x', 10), ('y', 20), ('z', 30)]

#A
# dict1 = {'a': 10, 'b': 20}
# dict2 = {'b': 5, 'c': 15}
# for key in dict1:
#     result = dict1.copy()
#     for key in dict2:
#         if key in result:
#             result[key] += dict2[key]
#         else:
#             result[key] = dict2[key]
# print(result)

#B
# kortez = (1, 2, 2, 3, 3, 3)
# temp = {}
# for num in kortez:
#     if num in temp:
#         temp[num] += 1
#     else:
#         temp[num] = 1

# print(temp)

#C
# dict1 = {'apple': 5, 'banana': 3, 'watermelon': 7}
# result = 0
# max_len = 0
# for i in dict1:
#     key_len = len(i)
#     if key_len > max_len:
#         max_len = key_len
#         result = i
# print(result)

#D
# import random
# numbers = (1, 2, 3, 4, 5)
# shuffled_list = list(numbers)
# random.shuffle(shuffled_list) 
# shuffled_tuple = tuple(shuffled_list)
# print(shuffled_tuple)

#E
# dict1 = {'x': 10, 'y': 20, 'z': 30}
# tuples_list = []
# for i in dict1:
#     tuples_list.append((i, dict1[i]))

# print("Список кортежей:", tuples_list)