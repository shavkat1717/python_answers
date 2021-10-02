<<<<<<< HEAD
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars=['toyota', 'mazda','hyundai', 'gm','kia']
print("1-usul bo'yicha:\n")
for car in cars:
    
    if car=='gm':
        print(car.upper())
    else: 
        print(car.title())

#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
print("\n2-usul bo'yicha:\n")
for car in cars:
    
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
login=input("Dear user! please enter login: \t =>")
if login.lower() == 'admin':
    print(f"Xush kelibsiz, {login.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz {login.title()}!")        
    
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son1=int(input("1-sonni kiriting:\t=>")) 
son2=int(input("2-sonni kiriting:\t=>"))  
if son1==son2:
    print("Sonlar teng")
else:
    print("sonlar bir-biriga teng emas")    

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
son=int(input("Istalgan sonni kiriting:\t=>")) 
if son<0:
    print("Ushbu son manfiy")
else:
    print("Ushbu son musbat")
    
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son0=int(input("Istalgan sonni kiriting:\t=>")) 
if son>0:
    print("Ushbu sonning ildizi ", son0**0.5," ga teng.")
elif son0<0:
=======
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars=['toyota', 'mazda','hyundai', 'gm','kia']
print("1-usul bo'yicha:\n")
for car in cars:
    
    if car=='gm':
        print(car.upper())
    else: 
        print(car.title())

#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
print("\n2-usul bo'yicha:\n")
for car in cars:
    
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
login=input("Dear user! please enter login: \t =>")
if login.lower() == 'admin':
    print(f"Xush kelibsiz, {login.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz {login.title()}!")        
    
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son1=int(input("1-sonni kiriting:\t=>")) 
son2=int(input("2-sonni kiriting:\t=>"))  
if son1==son2:
    print("Sonlar teng")
else:
    print("sonlar bir-biriga teng emas")    

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
son=int(input("Istalgan sonni kiriting:\t=>")) 
if son<0:
    print("Ushbu son manfiy")
else:
    print("Ushbu son musbat")
    
#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son0=int(input("Istalgan sonni kiriting:\t=>")) 
if son>0:
    print("Ushbu sonning ildizi ", son0**0.5," ga teng.")
elif son0<0:
>>>>>>> 2ae12e77ec2e28bfc3940738c8644128b2d93f2f
    print("Musbat son kiriting.")