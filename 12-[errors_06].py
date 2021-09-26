son = int(input("Istalgan butun son kiriting: \t => "))
for n in range(2,11):
    qoldiq=son%n
    if qoldiq==0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")