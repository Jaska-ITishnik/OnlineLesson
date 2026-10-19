"""
Funksiya (*args, **kwargs)
"""

# set va dict

# set -> toplam

# add, pop, difference, issubset, update

# dict - lug'at (dictionary)
"""
{
kalit: qiymat
}
kalit -> o'zgarmas(immutable)
qiymat -> farqi yo'q (immutable, mutable)

kalitlar -> har xil

mothods:
    get -> qiymat olish
"""

# d = {
#     1: "one",
#     2: "two",
#     3: "three",
# }
# print(d.get(10))
# print(d[10])

# codingbat string-2

# count_code

# word = "dcodexxcode"
# words = word.split("co")
# counter = 0
# for word in words:
#     if len(word) >= 2 and word[1] == "e":
#         counter += 1
# print(counter)

# new_str = word.replace("d", '').count("coe")
# print(new_str)


# xyz_there
# word = "abc.xyzxyz"
#
# print("xyz" in word.replace(".xyz", ''))

"""
Funksiya (*args, **kwargs)

DRY -> don't repat yourself (o'zingni o'zing takrorlama)

def {function_name} (argumentlar):
    return 
"""

"""
masala: Uchta son beriladi ularning 
        birinchi ikkitasini qo'shib va 
        natijani uchunchisiga ko'paytirish kerak
"""


# a = 1
# b = 10
# c = 15
# print((a + b) * c)

# d = 1
# e = 10
# f = 15
# print((d + e) * f)

def math_task(a, b, c):  # 3 ta majburiy argumentlar
    return (a + b) * c

# funksiyani chaqirish
# print(math_task(11, 10, 20))

# function types:
# 1 - qiymat qaytaruvchi -> return
# 2 - qiymat qaytarmaydigan -> void

# argument vs parametr

# print(math_task(40, 50 ,60))


# *args, **kwargs

# def summa(a, b, c, d, e, f, g, h, i)

# def summa(*args):
#     return sum(args)

# def summa(*args, **kwargs):
#     return sum(kwargs.values())
#
#
# print(summa(a=1, b=2, c=3))
