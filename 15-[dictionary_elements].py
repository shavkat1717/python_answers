# 1-masala:
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat",
    'false':"Yolg'on",
    'true':"Rost",
    'break':"Sikldan chiqish",
    'del': "Obyektni yo'qotish",
    'if': "Agar"
    }
for key, value in sorted(python_izohli_lugati.items()):
    print(f"{key.title()} - {value}")
# 2-masala:
capitals = {
    'usa':"Washington",
    'russia':"Moskow",
    'china':"Bejing",
    'iran':"Tegeran",
    'india':"New Dehli",
    'germany':"Berlin",
    'italy':"Rome",
    'france':"Paris",
    'great britain': "London",
    'uzbekistan': "Tashkent"
    }
print("The countries of the world:")
for country in sorted(capitals):
    print(country.upper())
print("\nThe capitals of countries:")
for capital in sorted(capitals.values()):
    print(capital.title())
country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = capitals.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"The capital of {country.upper()} is {capital.title()}.")
# 3-masala:    
menu = {
       'osh':18000,
       'beshteks':17000,
       'manti':20000,
       'chuchvara':16000,
       'xonim':15000,
       'non':4000,
       'choy':5000,
       'shashlik':12000,
       'somsa':6000,
       'tabaka':15000
       }
print("3 ta taom buyrutma qiling:\t=> ")   
buyrutmalar=[]
for n in range(3):
    buyrutmalar.append(input(f"{n+1}-taom:").lower())
for buyrutma in buyrutmalar:
    if buyrutma in menu:
        print(f"{buyrutma.title()} {menu[buyrutma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyrutma} yo'q.")











