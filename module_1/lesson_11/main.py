"""
1. Custom methods
2. Umumiy takrorlash
3. Kahoot test
"""


# my_upper

# print("Salom*&^%$".upper())
# print("A".isupper())

# text = input("Matn kiriting:")
# result = ""
# for i in text:
#     if 65 <= ord(i) <= 90 or not i.isalpha():
#         result += i
#     else:
#         result += chr(ord(i) - 32)
# print(result)
# print(ord("A"))
# print(chr(65))


# text = input("Matn kiriting:")
# my count
# print("Hello world!".count("hello"))


# def my_count(text, element):
#     if element not in text:
#         return 0
#     return len(text.split(element)) - 1
#
#
# print(my_count("Salom bolalar", 's'))


# print("Assalomu aleykum".split("aley"))
#
# print(my_count("Assalomu aleykum", "aley"))

# my replace
# print("Botirjon yaxshi bolajon".replace('xon', ""))


# print("Botirjon yaxshi bolajon".split('jon'))


# def my_replace(text, old, new):
#     if old not in text:
#         return text
#     words = text.split(old)
#     result = ""
#     for i, word in enumerate(words):
#         if i != 0 and word == "":
#             continue
#         result += word + new + " "
#     return result.strip()
#
#
# print(my_replace("Hello world Hello world", "world", "dunyo"))
# print("       Hello     ".strip())
# print("Hello world Hello".split("Hello"))
