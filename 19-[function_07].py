#Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def taqsimlash(x):
    """Ushbu funksiya foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiradi va natijalarni konsolga chiqaradi."""
    for n in range(2,11):
        if x%n==0:
            print(f"{x} soni {n} ga qoldiqsiz bo'linadi")
taqsimlash(70)