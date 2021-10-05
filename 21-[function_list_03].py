#Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.
talabalar = ['SHavkat Amirov', 'Firdavs Abduvaliyav', 'Islom Karimov', 'Shavkat Mirziyoyev']
def baholash(talabalar):
    baholar = {}
    for talaba in talabalar:
        baho = input(f"Talaba: {talaba.title()}ning bahosini kiriting:\t => ")
        baholar[talaba]=int(baho)
    return baholar       
baholar = baholash(talabalar)
print(baholar)
print(talabalar)