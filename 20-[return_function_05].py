#Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
def tub_sonlar(x,y):
    """Ushbu funksiya berilgan oraliqdagi tub sonlar ro'yxatini qaytaradi.(tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)"""
    tub_sonlar_toplami=[]
    for n in range(x, y+1):
        tub=True
        if (n==1):
            tub=False
        elif(n==2):
            tub=True
        else:
            for z in range(2,n):
                if (n%z==0):
                    tub=False
        if tub:
            tub_sonlar_toplami.append(n)
    return tub_sonlar_toplami
# Misol uchun: 100 dan 1000 gacha bo'lgan sonlar orasidan tub sonlarni topamiz:
print(tub_sonlar(100,1000))
