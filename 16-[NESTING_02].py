ika = {'ism':'Islom Karimov',
           'tyil':1938,
           'vyil':2016,
           'tjoy':'Samarqand',
           'asarlar':['Yuksak ma\'naviyat - yengilmas kuch','Vatan sajdagoh kabi muqaddasdir']
           }

ua = {'ism':'Usmonxon Alimov',
           'tyil':1950,
           'vyil':2021,
           'tjoy':'Samarqand',
           'asarlar':['Oilada farzand tarbiyasi','So\'ragan edingiz']
           }

shayx = {'ism':'Shayx Muhammad Sodiq Muhammad Yusuf',
           'tyil':1952,
           'vyil':2015,
           'tjoy':"Andijon",
           'asarlar':['Islom tarixi','Tavsiri hilol','Hadis va hayot','Oltin silsila']
           }

ay = {'ism':'Anvar qori Tursunov',
           'tyil':1958,
           'vyil':2018,
           'tjoy':"Toshkent",
           'asarlar':['Farzand tarbiyasi ma\'suliyati','Amallar niyatga qarab baholanadi']
           }

shaxslar = [ika, ua, shayx, ay]

for shaxs in shaxslar:
    ism = shaxs['ism']
    asarlar = shaxs['asarlar']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)
