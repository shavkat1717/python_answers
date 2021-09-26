mahsulotlar = ["un", "yog'", "sovun", "tuxum", "piyoz",
               "kartoshka", "olma", "banan", "uzum", "qovun"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: \t => "))
print(f"\nSizning bozorlik ro'yxatingiz: {savat}")
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
a=len(bor_mahsulotlar)
b=len(mavjud_emas)
if a>=1:
    print(f"\nSiz xohlagan {bor_mahsulotlar} mahsulotlar bizda mavjud:")
if a==5:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")
if b>=1:
    print(f"\nKechirasiz, bizda {mavjud_emas} yo'q:\n")
if b==5:
    print("Afsuski, siz so'ragan hech narsa bizda yo'q.")