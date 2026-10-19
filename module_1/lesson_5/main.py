"""
Set vs Dict differences and their primary methods
"""

# list methods, tuple

"""
            farqlari
1. [] -> list | () -> tuple
2. memory
3. list -> mutable | tuple -> immutable
"""

fruits = ["apple", "banana", "banana", "grape"]
# print(fruits.remove("apple"))
# print(fruits.pop(0))
# print(fruits.index("banana"))
# print(fruits.count("banana"))
# fruits.reverse()
# print(fruits[::-1])
"""
remove🟩
index🟩
count🟩
reverse🟩
extend🟩
"""
# fruits.extend(["olma", "behi", "shaftoli"])
# print(fruits)

# ints = [1, 2, 3]
# bad version (yomon versiya)

# if len(ints) >= 1 and ints[0] == ints[-1]:
#     print(True)
# else:
#     print(False)

# yaxshi versiya
# print(len(ints) >= 1 and ints[0] == ints[-1])

# print(sum([1, 2, 3]))


"""
Set vs Dict differences and their primary methods
"""
# int, str, float
# list, tuple

# set, dict
"""
        SET -> to'plam va uning xususiyatlari
1. toplam -> turli xil elementlar jamlanmasi
2. elementlar tartibsiz joylashgan
3. {} qavs yoki set() orqaliy yaratiladi
4. ichidagi element o'zgarmas bo'lishi kerak
"""
# print(names)

# set methods
# print(*[i for i in set().__dir__() if not i.startswith("__")])

names = {"Ali", "Jahongir", "Azamat"}  # shuffle
# names.add('Botirjon')
# print(names)

my_courses = {"english", "math", "japan"}
your_courses = {"english", "IT", "china"}
# print(names.pop())
# my_courses.update(["english"])
# print(my_courses)
"""
add🟩
clear🟩
copy🟩
discard🟩
difference🟩
pop🟩
remove🟩
union🟩
update🟩
difference_update
intersection
intersection_update
isdisjoint
issubset
issuperset
symmetric_difference
symmetric_difference_update
"""

# hometask

"""
8-masala. Majburiy fanlar
Talaba barcha majburiy fanlarni tanlagan yoki tanlamaganini aniqlang.
required_courses = {"Python", "English", "Math"}
student_courses = {"Python", "English", "Math", "Django", "Git"}
Natija True yoki False bo‘lishi kerak.
"""

# issubset => ichida bormi?

# required_courses = {"Python", "English", "Sport"}
# student_courses = {"Python", "English", "Math", "Django", "Git"}
# print(required_courses.issubset(student_courses))


# Dict -> dictionary
"""
str, int, float, list, tuple, set, dict
"""
"""
olma(kalit) - apple(qiymat)
qovun - melon
tarvuz - watermelon
"""

# print(*[i for i in dict().__dir__() if not i.startswith("__")])

numbers = {
    1: "one",
    2: "two",
    3: "three"
}
# print(numbers.get(4, "Bunday kalit mavjud emas!"))
# print(numbers[4])

# numbers.pop(1)
# print(numbers.items())
# numbers.clear()
# numbers.update({2: "ikki"})
# print(numbers)
# numbers.setdefault(4, "ikki")
# numbers.pop(1)
# numbers.pop(2)
# print(numbers)
# print(numbers.fromkeys("salom", 10))

"""
get🟩
pop🟩
keys🟩
items🟩
values🟩
clear🟩
copy🟩
update🟩
setdefault🟩
popitem🟩
fromkeys🟩
"""

"""
            Dict
1. Kalitlar🔑 har doim o'zgarmas ma'lumot turlari bo'ladi
        int, str, float, tuple
2. Qiyat ixtiyoru turdagi ma'lumot bo'lishi mumkin
        int, str, float, tuple, list, set, dict, complex
"""

# numbers = {
#     10.2: "one",
#     2: "two",
#     3: "three"
# }
# print(numbers[10.2])
