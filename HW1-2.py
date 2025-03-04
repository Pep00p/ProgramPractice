# Задание 1 (2 балл) Ввод-вывод

# a) Дана сторона квадрата a. Найти его площадь S = a^2.
# b) Дана площадь S круга. Найти его диаметр D и длину L окружности, ограничивающей этот круг, учитывая, что L = 2·π·R, S = π·R^2. 
# В качестве значения π использовать 3.14.
# c) Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов, потом обязательно двузначное количество минут, 
# затем обязательно двузначное количество секунд. 
# Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

# Задание 2 (3 балл) Условный оператор

# a) Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае вычесть из него 2. Вывести полученное число.
# b) Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел.
# c) Билет на одну поездку в метро стоит 15 рублей, билет на 5 поездок стоит 70 рублей, билет на 10 поездок стоит 125 рублей, 
# билет на 20 поездок стоит 230 рублей, билет на 60 поездок стоит 440 рублей. 
# Пассажир планирует совершить n поездок. Определите, сколько билетов каждого вида он должен приобрести, 
# чтобы суммарное количество оплаченных поездок было не меньше n, а общая стоимость приобретенных билетов – минимальна.


# Задание 1 (2 балл) Ввод-вывод
selected_task = int(input("Введите номер задания: "))
if selected_task == 1:
    selected_second_task = str(input("Введите букву задания: "))
    if selected_second_task == 'a':
        #a)
        square_side = int(input("Введите сторону квадрата: "))
        space = square_side**2
        print('Периметр данного квадрата: ', space)

    elif selected_second_task == 'b':
        #b)
        space_sirc= int(input())
        pi = 3.14
        rad= (space_sirc/pi)**0.5
        diam = rad*2
        leight = 2 * pi * rad
        print("Диаметр: ",diam,"Длина: ", leight)




    elif selected_second_task =='c':
        #c
        seconds_all = int(input("Введите количество секунд: "))
        hours = (seconds_all//3600)%12 or 12
        minutes = (seconds_all%3600)//60
        seconds = seconds_all%60
        print(f"{hours}:{minutes:02}:{seconds:02}")

    else:
        print("Нет такого подпункта >:()")

# Задание 2 (3 балл) Условный оператор
elif selected_task == 2:
    selected_second_task = str(input("Введите букву задания: "))
    if selected_second_task == 'a':
        #a
        number = int(input("Введите число: "))
        if number > 0:
            number +=1
            print(number)
        elif number < 0:
            number-= 2
            print(number)
        else:
            print("Поздравляю! Вы ввели 0!")

    elif selected_second_task == "b":
        #b
        first_number, second_number, third_number = map(int, input("Введите числа через пробел: ").split())
        if first_number > second_number and first_number>third_number:
            print(first_number)
        elif second_number > first_number and second_number>third_number:
            print(second_number)
        else:
            print(third_number)

    elif selected_second_task =="c":
        #c
        n_trip_count = int(input("Введите количество поездок: "))
        one_trip_ticket=five_trip_ticket=ten_trip_ticket=twelve_trip_ticket=sixteen_trip_ticket = 0

        if n_trip_count >= 60:
            sixteen_trip_ticket = n_trip_count // 60
            n_trip_count %= 60
        if n_trip_count >= 20:
            twelve_trip_ticket = n_trip_count // 20
            n_trip_count %= 20
        if n_trip_count >= 10:
            ten_trip_ticket = n_trip_count // 10
            n_trip_count %= 10
        if n_trip_count >= 5:
            five_trip_ticket = n_trip_count // 5
            n_trip_count %= 5
        if n_trip_count >= 1:
            one_trip_ticket = n_trip_count
        print(one_trip_ticket, five_trip_ticket, ten_trip_ticket, twelve_trip_ticket, sixteen_trip_ticket)

    else:
        print("Нет такого подпункта >:()")