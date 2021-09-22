#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
son=float(input("Istalgan sonni kiriting: \t =>"))
print(f" {son} ning kvadrati:", (son**2)," ga teng.")
print(f" {son} ning kubi:", (son**3)," ga teng.")

#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
son=int(input("Hurmatli fuqaro yoshingiz nechada? \t =>"))
print(f" Demak siz :", (2021-son)," - yilda tug'ilgansiz, topdimmi ?")

#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
son1=float(input("Birinchi sonni kiriting: \t =>"))
son2=float(input("Ikkinchi sonni kiriting: \t =>"))
print(f"{son1} + {son2} =", (son1)+(son2))
print(f"{son1} - {son2} =", (son1)-(son2))
print(f"{son1} * {son2} =", (son1)*(son2))
print(f"{son1} / {son2} =", (son1)/(son2))
