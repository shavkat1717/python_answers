mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
    mahsulotlar[mahsulot] = int(narh)
    javob = input("Yana mahsulot qo'shasizmi? ( ha / yo'q ): ")
    if javob != 'ha':
        break
print('Siz xohlagan mahsulotlar:')
print(mahsulotlar, end=" ")