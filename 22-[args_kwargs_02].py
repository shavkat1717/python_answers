#Talabalar haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya yozing. Talabaning ismi va familiyasini majburiy argument, qolgan ma'lumotnilar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def malumotlar(ism, familiya, **yana_xohlagancha):
    yana_xohlagancha['ism']=ism
    yana_xohlagancha['familiya']=familiya
    return yana_xohlagancha
chaqaloq=malumotlar('Soliha', 'Yorqinova', yili=2021, oyi='yanvar', sanasi=6, vatani='O\'zbekiston', viloyati='Buxoro', tumani='Jondor', otasining_ismi='Shavkatovna')
print(chaqaloq)