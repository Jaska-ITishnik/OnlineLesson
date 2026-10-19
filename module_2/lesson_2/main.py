"""
20 -> 50
"""
"""
1 bayt = 8 bit
1 Kbayt = 1024 bayt
1 Mbayt = 1024 * 1024 bayt
1 Gbayt = 1024 * 1024 * 1024 bayt
1 Tbayt = 1024 * 1024 * 1024 * 1024 bayt
"""

# 17 - question
# file_memory = int(input("enter file memory in bytes:"))
# print(f"{file_memory} bayt = {file_memory / 1024} Kbayt")


# 25 - question
"""
750 Kbayt          ->     1 sekund
1.8 * 1024 * 1024  ->      x sekund

750 * x = 1.8 * 1024 * 1024 * 1
x = 1.8 * 1024 * 1024 / 750
"""
# print(round(1.8 * 1024 * 1024 / 750, 2))


# 28 - question

# soning raqamlari ko'paytmasi, yig'indisi
"""
nechta raqam bor? -> 10 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
nechta son -> infinity


7894 -> (7 + 8 + 9 + 4) = 28 
7894 -> (7 * 8 * 9 * 4) = ? 
"""

# bad version (raqamlar yig'indisi)
# num = input("enter number:")
# result = 0
# for i in num:
#     result += int(i)
# print(result)

# bad version (raqamlar ko'paytmasi)
# num = input("enter number:")
# result = 1
# for i in num:
#     result *= int(i)
# print(result)

# good version
# 45 // 10 = 4

# num = int(input("enter number:"))
# result = 1
# while num:
#     result *= num % 10
#     num = num // 10
# print(result)


# 32 - question

# num = int(input("enter number:"))
# while num:
#     if num % 10 == 3:
#         print(True)
#         break
#     num = num // 10  # 126
# else:
#     print(False)


# 34 - question
# month_number = int(input("enter the month number:"))
# if month_number in {1, 2, 12}:
#     print("Qish⛄")
# elif month_number in {3, 4, 5}:
#     print("Bahor💐")
# elif month_number in {6, 7, 8}:
#     print("Yoz🍧")
# elif month_number in {9, 10, 11}:
#     print("Kuz🍁")
# else:
#     print("bunday oy mavjud emas!")


# score = int(input("enter score:"))
# if 0 <= score <= 54:
#     print("2 baho")
# elif 55 <= score <= 70:
#     print("3 baho")
# elif 71 <= score <= 84:
#     print("4 baho")
# elif 85 <= score <= 100:
#     print("5 baho")
# else:
#     print("bunday baho yo'q")


# 40 - question

# a = int(input("a = "))
# if a > 0:
#     print(a + 1)
# elif a < 0:
#     print(abs(a) + 2)
# else:
#     print(0)
"""
module -> uzunlik
|5| = 5
|-4| = 4
|0| = 0
"""
