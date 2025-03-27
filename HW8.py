# Вариант 2
# a) Напишите функцию `gcd(a, b)`, которая принимает два числа `a` и `b` и возвращает их наибольший общий делитель.
# Ввод	Вывод
# 12 18	6

# б) Напишите функцию `next_prime(n)`, которая принимает число `n` и возвращает следующее простое число, большее или равное `n`.
# Ввод	Вывод
# 10	11

# c) Напишите функцию `fibonacci(n)`, которая возвращает `n`-е число Фибоначчи.
# Ввод	Вывод
# 5	5

#A
# def gcd(a, b):
#     while b:
#         temp = a  
#         a = b     
#         b = temp % b
#     return a
# print(gcd(12,18))

#B
# def proverka(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def next_prime(n):
#     temp = n
#     while not proverka(temp):
#         temp += 1
#     return temp

#C
# def fibonacci(n):
#     if n <= 0:
#         print("n должно быть положительным числом")
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
    
#     a, b = 1, 1
#     for i in range(3, n + 1):
#         a, b = b, a + b
#     return b
# print(fibonacci(5))  