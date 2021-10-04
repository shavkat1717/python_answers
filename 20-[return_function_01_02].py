def saylov_chi(ism, familiya, t_yil, t_joy, email='',tel=None):
    """Ushbu funksiya saylovchi haqidagi ma'lumotlarni lug'at ko'rinishida qaytaradi"""
    saylovchi = {'ism':ism,
             'familiya':familiya,
             'tyil':t_yil,
             'yoshi':2021-t_yil,
             'tjoy':t_joy,
             'email':email,
             'telefon':tel}
    return saylovchi
print("\nSaylovchi haqida ma'lumotlarni kiriting.")
saylovchilar =[]
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    t_yil = int(input("Tug'ilgan yili: "))
    t_joy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    tel = int(input("Telefon raqami: "))
    saylovchilar.append(saylov_chi(ism, familiya, t_yil, t_joy, email, tel))
    javob = input("Davom etasizmi? (ha / yo'q)")
    if javob !='ha':
        break
print("Saylovchilar:")
for saylovchi in saylovchilar:
    print(f"{saylovchi['ism'].title()} {saylovchi['familiya'].title()}, " 
          f"{saylovchi['yoshi']} yoshda, telefoni: {saylovchi['telefon']}.")