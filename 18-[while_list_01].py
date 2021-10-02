print("\nMijozlardan buyrutmalar qabul qilamiz!")
buyrutmalar=[]
b=1
#buyrutma=input('Qanday taomlar yeyishni xohlaysiz?')
while True:
    taom=f"{b} - taomni kiriting:\t => "
    taomlar=input(taom)
    buyrutmalar.append(taomlar)
    yana=input("Yana nimadir xohlaysizmi? (ha / yo'q )")
    b+=1
    if yana !='ha':
        break
print("\nSiz xohlagan taomlar:\n")
print(buyrutmalar)

#1-masala:
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz!")
# ismlar=[]
# n=1
# while True:
#     savol=f"{n} - do'stingizni kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash=input("Yana do'st qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash !='ha':
#         break  
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
# Agar lug'at={} ... Bu lug'at
# Agar ro'yxat=[] ... Bu ro'yxat

#2-masala:
# dostlar={}
# ishora= True
# while ishora:
#     ism=input("Do'stingizni ismini kiriting: ")
#     yosh=input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)
#     javob=input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob=="yo'q":
#         ishora=False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# #3-masala
# cars=['Malibu','Nexia','Tahoe','Nexia','Trailblazer','Nexia','Captiva','Onix','Nexia']
# car='Nexia'
# print(cars)
# while car in cars:
#     cars.remove(car)
# print(cars)
# talabalar=['Habib','Shahzod','Abdurahmon','Nuriddin sohib','Ilnur','Shavkat']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba]=int(baho)
# print(baholangan_talabalar)

# for taom in taomlar:
#     print(f"{taom.title()}")
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz!")
# ismlar=[]
# n=1
# while True:
#     savol=f"{n} - do'stingizni kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash=input("Yana do'st qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash !='ha':
#         break  
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())