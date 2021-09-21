#Quyidagi o'zgaruvchilarni yarating: 
respublika="O'zbekiston"
viloyat="Buxoro"
tuman="Jondor"
mahalla="Chorzona"

#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
print(f"Men {respublika} Respublikasi, {viloyat} viloyati, {tuman} tumani, {mahalla} mahallasida yashayman.")

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
respublika2=input("Sizning davlatingiz:\t =>")
viloyat2=input("Sizning viloyatingiz:\t =>")
tuman2=input("Sizning tumaningiz:\t =>")
mahalla2=input("Sizning mahallangiz:\t =>")
print("Demak siz ", respublika2 ," Respublikasi,", viloyat2 ," viloyati,", tuman2, " tumani,", mahalla2, " mahallasida yashaysiz.")

#Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print("Demak siz ", respublika2 ," Respublikasi,\n", viloyat2 ," viloyati,\n", tuman2, " tumani,\n", mahalla2, " mahallasida yashaysiz.")

#Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
print(f"Demak siz {respublika2} Respublikasi, {viloyat2} viloyati, {tuman2} tumani, {mahalla2} mahallasida yashaysiz.")
manzil=(f"Demak siz {respublika2} Respublikasi, {viloyat2} viloyati, {tuman2} tumani, {mahalla2} mahallasida yashaysiz.")
print(manzil)
print(manzil.upper())
print(manzil.title())
print(manzil.lower())
print(manzil.capitalize())