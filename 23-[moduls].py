# 23-dars bo'yicha uyga vazifa yo'q.
# [1] main.py
# import avto_info_mod

# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)

# import avto_info_mod as aim

# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)

# from avto_info_mod import avto_info, info_print

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)

# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)

# from avto_info_mod import *

# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)

# avtolar = avtoil.avto_kirit()

# for avto in avtolar:
#     avtoil.info_print(avto)
# [2] avto_info_mod
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#     avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")    
#         #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#         #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
#         # Yana avto qo'shish-qo'shmaslikni so'raymiz
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob=='no':
#             break
#     return avtolar

# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
#           f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#           f"{avto_info['yil']}-yil, {avto_info['narh']}$")

# [3] codes math function
# import math
# x=400
# # print(math.sqrt(x))
# # print(math.pow(6,2))
# # print(math.pi)
# print(math.log2(8))
# print(math.log10(100))

# [4] codes random function

# import random as r

# #randint()
# son = r.randint(10,50)
# print(son)

# # choice()
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))
# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))

# # shuffle()
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)