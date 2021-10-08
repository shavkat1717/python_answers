def tubmi(x):
    if x%2==0 or x<2: return False # Son juft yoki 2 dan kichik bo'lsa
    if x==2 or x==3 : return True # Son 2 yoki 3 bo'lsa
    for i in range(3,x,2):         
        if x%i==0:
            return False
    return True
tub_sonlar = list(filter(tubmi,range(100)))
print(tub_sonlar)