# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.
def kattalashtirish(ismlar):
    """Ushbu funksiya matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiradi """
    for ism in range(len(ismlar)):
        ismlar[ism]=ismlar[ism].title()
ismlar=['firdavs', 'shavkat','tavakkal','shuhrat','muhammad','bahodir']
kattalashtirish(ismlar)
print(ismlar)