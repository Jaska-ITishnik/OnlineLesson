"""
Funksiyalar turlari(recursive, lambda, filter, map, reduce, zip)
"""

# def function_name(*args, **kwargs):
#     pass

""" 
function return -> qiymat
void -> print
"""

# *args and **kwargs

# coddingbat list - 2

"""
(4 + 5 + 6 + 7 + 8 + 9) / 6
"""
# numbers = [1, 1, 5, 5, 10, 8, 7]
# maxi = max(numbers)
# mini = min(numbers)
# summa = 0
# for number in numbers:
#     if number not in (maxi, mini):
#         summa += number
# print(summa / (len(numbers) - 2))


# has_22
# numbers = [2, 1, 2]
# for number in numbers:
#     print(number)


# for i in range(1, len(numbers)):
#     if numbers[i - 1] == 2 and numbers[i] == 2:
#         print(True)
#         break
# else:
#     print(False)


# home tasks

"""
6. Mahsulot yaratish — **kwargs
Mahsulot ma’lumotlarini qabul qiladigan create_product() funksiyasini yarating. name va price mavjudligini tekshiring. Ulardan biri yo‘q bo‘lsa, xatolik xabarini chiqaring.
create_product(name="Laptop", price=8500000, brand="Lenovo")
create_product(name="Telefon")

7. Talaba natijasini hisoblash — **kwargs
Fan nomlari va baholarini qabul qilib, talabaning o‘rtacha bahosini hisoblaydigan student_result() funksiyasini yozing.
student_result(math=5, english=4, python=5)
# O‘rtacha baho: 4.67

"""


# def create_product(price, name="pc", brand="Lenovo"):
#     return f"""
# Nomi: {name}
# Narxi: {price}
# Brand: {brand}
# """
#
#
# print(create_product(name="Laptop", price=7_200_000, brand="HP"))

# 7 - avg value

# def student_result(**kwargs):
#     grades = kwargs.values()
#     return round(sum(grades) / len(grades), 2)
# print(student_result(math=5, english=5, history=4))