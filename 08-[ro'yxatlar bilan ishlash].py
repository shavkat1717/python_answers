#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["Uzbekistan","Russia", "China", "USA", "Turkiye", "Iran"]
print(davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring
print(f"Elementlar soni: {len(davlatlar)} ta.")

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(f"Tartiblangan ro'yxat: {sorted(davlatlar)}")

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(f"Teskari tartib: {sorted(davlatlar, reverse=True)}")

#Asl ro'yxatni qaytadan konsolga chiqaring
print(f"Asl ro'yxat: {davlatlar}")

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(f"Asl ro'yxatni teskari tartibi: {davlatlar}")

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(f"Alifbo bo'yicha: {davlatlar}")
davlatlar.sort(reverse=True)
print(f"Teskari alifbo bo'yicha: {davlatlar}")

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
print("\n120 dan 1200 sonlari orasidagi juft sonlar ro'yxati:\n")
sonlar = list(range(120,1200,2))
print(sonlar)
#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(f" \nYuqoridagi ro'yxatdagi sonlar yig'indisi S = {sum(sonlar)} ga teng.")

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(f"\nRo'yxatdagi eng katta va eng kichik son o'rtasidagi ayirma: {max(sonlar)-min(sonlar)} ga teng.")

#Ro'yxatdagi elementlar sonini hisoblang
print(f"\nRo'yxatdagi elementlar soni: {len(sonlar)} ta.")

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(f"\nIlk 20 ta qiymat: \n \n {sonlar[:20]}")
print(f"\nO'rtadagi 20 ta qiymat: \n\n {sonlar[-20:]}")
print(f"\nEng oxiridagi 20 ta qiymat: \n \n {sonlar[520:540]}")

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','manti','shashlik','halim','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('qozonkabob')
nonushta.remove('shashlik')
nonushta.remove('halim')
nonushta.append('qaymoq')
nonushta.append('issiq non')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(f"\n Taomlar:\n\n {taomlar}")
print(f"\n Nonushta: \n \n {nonushta}")

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
#nonushta[0] = "qaymoq va non" deb o'zgartirish kiritolmaymiz, sababi: tuple() ya'ni ro'yxatimizni o'zgarmasga aylantirganmiz
