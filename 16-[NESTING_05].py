ika = {'ism':'Islom Karimov',
           'tyil':1938,
           'vyil':2016,
           'tjoy':'Samarqand'
           }

ua = {'ism':'Usmonxon Alimov',
           'tyil':1950,
           'vyil':2021,
           'tjoy':'Samarqand'
           }

shayx = {'ism':'Shayx Muhammad Sodiq Muhammad Yusuf',
           'tyil':1952,
           'vyil':2015,
           'tjoy':"Andijon"
           }

ay = {'ism':'Anvar qori Tursunov',
           'tyil':1958,
           'vyil':2018,
           'tjoy':"Toshkent"
           }

shaxslar = [ika, ua, shayx, ay]

for shaxs in shaxslar:
    ism = shaxs['ism']
    tyil = shaxs['tyil']
    vyil = shaxs['vyil']
    tjoy = shaxs['tjoy']
    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
          f"{vyil-tyil} yil umr ko'rgan.")