print("\nMijozlardan buyrutmalar qabul qilamiz!")
buyrutmalar=[]
b=1
#buyrutma=input('Qanday taomlar yeyishni xohlaysiz?')
while True:
    taom=f"{b} - taomni kiriting:\t => "
    taomlar=input(taom)
    buyrutmalar.append(taomlar)
    yana=input("Yana nimadir xohlaysizmi? (ha / yo'q )")
    b+=1
    if yana !='ha':
        break
print("\nSiz xohlagan taomlar:\n")
print(buyrutmalar)

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

while buyrutmalar:
    buyrutma = buyrutmalar.pop()
    if buyrutma in mahsulotlar.keys():
        narx = mahsulotlar[buyrutma]
        print(f"{buyrutma.title()} - {narh} so'm\n")
    else:
        print(f"Bizda {buyrutma} yo'q")