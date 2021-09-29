print("\nSizning yoqtirgan kitoblaringiz !\n")
savol="Yoqtirgan kitobingizni kiriting: => "
savol+="\n(Dasturni to'xtatish uchun 'stop' deb yozing.): "
qiymat=''
while qiymat !='stop':
    qiymat=input(savol)
    if qiymat !='stop':
        print(f'Sizning sevimli kitobingiz: "{qiymat.title()}"')
print('Dastur tugadi.')