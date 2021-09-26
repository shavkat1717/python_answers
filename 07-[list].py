#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar=['Muhammad', 'Tavakkal', 'G\'ayrat']

#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
print(f" Salom {ismlar[0]} bugun choyxona bormi?\n {ismlar[1]} choyxonaga boramizmi? \n {ismlar[2]} do'stim sen ham albatta kel.")

#sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
sonlar=[17, -5, 0.36, -25.48, 94_929_75_17]

#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
nisbat=sonlar[0]/sonlar[2]
print(nisbat)
yigindi=sonlar[1]+sonlar[3]
print(yigindi)
sonlar[0]=sonlar[0]+10
print(sonlar)
sonlar[2]=3.14159
print(sonlar)

#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
t_shaxslar=['Bobur', 'Imom al Buxoriy', 'Ibn Sino', 'Najmiddin Kubro']
z_shaxslar=['Ilon Mask', 'Pavel Durov', 'Alisher Usmonov', 'Shavkat Amirov']

#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan suhbat qilishni istar edim.")

#friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends=[]
friends.append("Habib")
friends.append("Shahzod")
friends.append("Abdurahmon")
friends.append("Nuriddin")
friends.append("Ilnur")
friends.append("Hamid")
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove("Hamid")
friends.remove("Abdurahmon")
print(friends)

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append("Abdulloh")
friends.insert(3, "Firdavs")
friends.insert(6,"Ahror")
print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar=[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
print(mehmonlar)