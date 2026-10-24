"""
40 -> 70 GACHA
"""

# 46 - question

# bad version
# a = 402
# numbers = []
# while a:
#     numbers.append(a % 10)
#     a //= 10
# print(max(numbers))

# good version
# a = 402
# maxi = a % 10
# while a:
#     if maxi < a % 10:
#         maxi = a % 10
#     a //= 10
# print(maxi)


# 47 - question

# 11 -> o'n bir
# 25 -> yigirma besh

# birlar = [
#     "bir", "ikki", "uch",
#     "to'rt", "besh", "olti",
#     "yetti", "sakkiz", "to'qqiz"
# ]
# onlar = [
#     "o'n", "yigirma", "o'ttiz",
#     "qirq", "ellik", "oltmish", "yetmish"
# ]
# number = int(input("10 - 70 oqalig'ida son kiriting:"))  # 12
# if number not in range(10, 71):
#     print("sonlar oraliqda mavjud emas!")
# else:
#     last = number % 10
#     first = number // 10
#     print(f"{onlar[first - 1]} {birlar[last - 1]}")


# 48 - question
# a, b, c = map(int, input("a b c = ").split())
# if a > 0 and b > 0 and c <= 0:
#     print(a + b)
# elif b > 0 and c > 0 and a <= 0:
#     print(b + c)
# elif a > 0 and c > 0 and b <= 0:
#     print(a + c)
# else:
#     print(a * b * c)


# 52 - question
"""
1 asr -> 100 yil

1400 yil -> 14 asr
"""
# year = int(input("enter the year:"))
# if year % 100:
#     print(year // 100 + 1, 'asr')
# else:
#     print(year // 100, "asr")
#

# 71 - question
"""
a ............ b
1 ............ 10
    23456789
"""
# a, b = map(int, input("a b = ").split())
# for i in range(a + 1, b):
#     print(i, end=" ")
# print(sum(range(a + 1, b)))

# 74 - question
# for i in range(1, 101, 2):
#     if i % 3 == 0 and i % 5 != 0:
#         print(i)


# 77 - question
# result = 1
# counter = 0
# while True:
#     number = int(input("number = "))
#     if number == 0 and counter == 0:
#         result = 0
#     if number == 0:
#         break
#     result *= number
#     counter += 1
# print(result)

# 79 - question
"""
10 ..... 98 99
18, 28, 38, 48 ..... 80, 81, 82, 83, 84, ... 89, 98
"""

# for i in range(10, 100):
#     if i % 10 == 8 or i // 10 == 8:
#         print(i, end=' ')
