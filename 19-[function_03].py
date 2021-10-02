#Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juft_yoki_toq(son):
    """ Ushbu funksiya foydalanuvchidan son olib, mazkur sonning juft yoki toqligini konsolga chiqaradi."""
    if son%2==0:
        print(f"{son} soni juft son hisoblanadi.")
    else:
        print(f"{son} soni toq son hisoblanadi.")
juft_yoki_toq(17)
juft_yoki_toq(128)