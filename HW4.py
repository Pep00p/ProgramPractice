# Вариант 2
# a) Удаление элементов, которые встречаются только один раз: Дан список чисел, удалите из него все элементы, которые встречаются только один раз.
# Ввод	Вывод
# [4, 3, 5, 3, 4, 4, 7, 8]	[4, 3, 3, 4, 4]

# б) Наибольшая последовательность подряд идущих одинаковых чисел: Напишите функцию, которая принимает список чисел и возвращает наибольшую последовательность подряд идущих одинаковых чисел в этом списке. Если таких последовательностей несколько, вернуть первую.
# Ввод	Вывод
# [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5]	[4, 4, 4, 4]

# c) Сортировка списка по количеству вхождений элементов: Дан список чисел. Отсортируйте его так, чтобы элементы с большим количеством вхождений шли раньше элементов с меньшим количеством вхождений. При равном количестве вхождений сохранить их исходный порядок.
# Ввод	Вывод
# [4, 3, 3, 2, 2, 2, 1]	[2, 2, 2, 3, 3, 4, 1]

#A
# array = [4, 3, 5, 3, 4, 4, 7, 8]
# array2 = []
# temp = {}
# for num in array:
#     if num in temp:
#         temp[num] += 1
#     else:
#         temp[num] = 1
# for num in array:
#     if temp[num] > 1:
#         array2.append(num)

# print(array2)

#B
# array = list(map(int, input().split()))
# max_len = 0
# curr_len = 1
# max_seq = []
# curr_seq = [array[0]]
# for i in range(1, len(array)):
#     if array[i] == array[i - 1]:
#         curr_len += 1
#         curr_seq.append(array[i])
#     else:
#         if curr_len > max_len:
#             max_len = curr_len
#             max_seq = curr_seq[:]
#         curr_len = 1
#         curr_seq = [array[i]]
# if curr_len > max_len:
#     max_seq = curr_seq
# print(max_seq)

#c
input_list = [4, 3, 3, 2, 2, 2, 1]

counts = {}
for num in input_list:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for i in range(len(input_list)):
    for j in range(i + 1, len(input_list)):
        if counts[input_list[i]] < counts[input_list[j]]:
            input_list[i], input_list[j] = input_list[j], input_list[i]

print("Отсортированный список:", input_list)


        
