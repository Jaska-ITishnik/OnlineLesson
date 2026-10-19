"""
Funksiyalar turlari(recursive, lambda, filter, map, reduce, zip)
"""

numbers = [1, 4, 5, 10, 13]

# recursive function
# def say_hi():
#     print("Assalomu aleykum")
#     say_hi()

# say_hi()

"""
n! => n faktorial
n! = 1 * 2 * 3 * 4 * 5 * 6 * 7 ... * n

4! = 1 * 2 * 3 * 4
7! = 1 * 2 * 3 * 4 * 5 * 6 * 7
"""

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
#
#
# print(factorial(6))

"""
                            Recursion
1. Rekursiya chekliy bo'lishi kerak (to'xtash shart)

ikki qismdan tashkil topgan bo'ladi
    I) base case (sodda qismi) => to'xtash sharti
    II) iterative case (takrorlanuvchi qismi)
"""

# def factorial_recursive(n):
#     if n == 1:
#         return 1
#     return n * factorial_recursive(n - 1)  # 6 * (5 * (4 * (3 * (2 * 1))))
#
#
# print(factorial_recursive(6))


# lambda function

# def summa(a, b):
#     return a + b

# summa = lambda a, b: a + b

# print(summa(1, 10))

# def greeting(name):
#     return f"Assalomu aleykum {name}"

# greeting = lambda name: f"Assalomu aleykum {name}"
# print(greeting("Botirjon"))

# age = int(input("Yoshni kiriting:"))
# print("Xush kelibsiz!" if age > 18 else "Sizga kirish mumkin emas!")


# age = input("age = ")
#
#
# def age_checker(age):
#     if age >= 18:
#         print("Xush kelibsiz!")
#     else:
#         print("Sizga kirish mumkin emas!")
#
#
# print(age_checker(age))


# filter, map, reduce, zip

# 1 dan 100 gacha bo'lgan sonlar
# orasidan 3 ga bo'linadigan sonlarni toping
# print(list(filter(lambda number: number % 3 == 0 and number % 5 != 0, range(1, 101))))

# pupils = ["Anvar", "Azim", "Botir", "Karimjon", "Davron"]
# print(list(filter(lambda pupil: pupil.startswith("A"), pupils)))


# map
# print(list(map(str, [1, 2, 3, 4])))

# numbers = ["1", "2", "3", "4"]
# for i in range(0, len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers)


# reduce va zip
# 1 - version
# print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

# 2 - version
# result = 1
# for i in [1, 2, 3, 4, 5]:
#     result *= i
# print(result)

# zip

# names = ['Ali', 'Vali', 'Kamol']
# ages = [20, 12, 25]
# height = [1.70, 1.65, 1.92]
# print(list(zip(names, ages, height)))
