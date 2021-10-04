#Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
def aylana(radius, p=3.14159):
    """Ushbu funksiya foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaradi"""
    aylana_elementlari={
        "radiusi": radius,
        "diametri": 2*radius,
        "uzunligi": 2*p*radius,
        "yuzasi": p*(radius**2)
        }
    return aylana_elementlari
while True:
    Aylana_elementlar=[]
    radius=float(input(f"Aylananing radiusini kiriting:\t=> "))
    Aylana_elementlar.append(aylana(radius))
    print(f"Aylana elementlari: {Aylana_elementlar}")
    javob = input("Yana biror radius kiritasizmi? (yes / no): ")
    if javob !='yes':
        break
print("Dastur tugadi!")