father= {
            'firstname':'Yorqin',
            'fullname':'Amirovich',
            'year':1970,
            'region':'Bukhara'
    }
mother= {
            'firstname':'Sabohat',
            'fullname':'Rahimovna',
            'year':1970,
            'region':'Bukhara'
    }
brother= {
            'firstname':'Shahboz',
            'fullname':'Yorqinovich',
            'year':1993,
            'region':'Bukhara'
    }
sister= {
            'firstname':'Chexrona',
            'fullname':'Yorqinovna',
            'year':2000,
            'region':'Bukhara'
    }
print(f" {father['firstname']} {father['fullname']} was born {father['year']} in {father['region']} !")
print(f" {mother['firstname']} {mother['fullname']} was born {mother['year']} in {mother['region']} !")
print(f" {brother['firstname']} {brother['fullname']} was born {brother['year']} in {brother['region']} !")
print(f" {sister['firstname']} {sister['fullname']} was born {sister['year']} in {sister['region']} !\n")
delicious= {
            'father':'osh',
            'mother':'manti',
            'brother':'shashlik',
            'sister':'chuchvara',
            'uncle':'sumalak'
    }
print(" My father's lovely meal is", delicious['father'],".")
print(" My mother's lovely meal is", delicious['mother'],".")
print(" My brother's lovely meal is", delicious['brother'],".")
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
kalit = input("Python kalit so'z (key words) kiriting: \t => ").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")