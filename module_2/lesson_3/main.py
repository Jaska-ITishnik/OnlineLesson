"""
20 -> 40
"""

# 27 - question
# n = int(input("n sekund = "))
# hour = n // 3600
# print(f"""
# kun: {hour // 24}
# Soat: {hour % 24}
# Minut: {n % 3600 // 60}
# Sekund: {n % 60}
# """)
# print(1 * 24 * 60 * 60 + 3600 + 60 + 1)
# print(n % 3600)


# 33 - question
# numbers = map(int, input("a b c d e = ").split())
# counter_zero = 0  # nol
# counter_pos = 0  # musbat
# counter_neg = 0  # manfiy
# for number in numbers:
#     if number > 0:
#         counter_pos += 1
#     elif number < 0:
#         counter_neg += 1
#     else:
#         counter_zero += 1
# print(f"""
# Nollar: {counter_zero} ta
# Manfiylar: {counter_neg} ta
# Musbatlar: {counter_pos} ta
# """)

# 36 - question
# a, b, c = map(int, input("a b c = ").split())
# if a == b == c:
#     print("=")
# elif a != b and b != c and a != c:
#     print(a, b, c)
# elif a == b:
#     print(c)
# elif b == c:
#     print(a)
# elif a == c:
#     print(b)


# 41 - question
# a, b, c = map(int, input("a b c = ").split())
# print(abs(a - b) >= 10 or abs(a - c) >= 10 or abs(b - c) >= 10)
"""
|-3| = 3
|3| = 3
"""

# 44 - question 456
# number = int(input("n = "))
# birlar = number % 10
# onlar = number // 10 % 10
# yuzlar = number // 100
# print(onlar - yuzlar == 1 and birlar - onlar == 1)
