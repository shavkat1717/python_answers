#Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def kopaytma(*sonlar):
    kopaytiruvchi = 1
    for son in sonlar:
        kopaytiruvchi*=son
    return kopaytiruvchi
print(kopaytma(5,17,8))