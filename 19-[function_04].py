#Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def taqqoslash(son1,son2):
    """Ushbu funksiya foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaradi. Agar sonlar teng bo'lsa "Sonlar teng" degan xabar chiqadi"""
    if son1>son2:
        print(f"{son1} > {son2}")
    elif son1<son2:
        print(f"{son1} < {son2}")
    else:
        print("Sonlar teng!")
taqqoslash(5, 7)
taqqoslash(18, 10)
taqqoslash(26, 26)