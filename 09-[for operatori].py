<<<<<<< HEAD
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Suhrob','Firdavs','Shahboz','Mirshod','Jasur']
for ism in ismlar:
    print(f"\t {ism.upper()} uchun yo'llangan xabar: \n Assalomu alaykum, {ism.title()}. Sizni ko'rganimdan xursandman!")

# Yuoqirdagi tsikl tugaganidan so'ng, 
# ekranga "Kod n marta takrorlandi" degan xabar chiqaring 
# (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning har bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?\t =>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
=======
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
ismlar = ['Suhrob','Firdavs','Shahboz','Mirshod','Jasur']
for ism in ismlar:
    print(f"\t {ism.upper()} uchun yo'llangan xabar: \n Assalomu alaykum, {ism.title()}. Sizni ko'rganimdan xursandman!")

# Yuoqirdagi tsikl tugaganidan so'ng, 
# ekranga "Kod n marta takrorlandi" degan xabar chiqaring 
# (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning har bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang,
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan 
# uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?\t =>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
>>>>>>> 2ae12e77ec2e28bfc3940738c8644128b2d93f2f
print(ismlar)