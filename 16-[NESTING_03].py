kinolar = {
    'g\'ayrat':['Ujas','Taksi','Jangchi'],
    'tavakkal':['Dunyo','Janob bin','Uch mushktyor'],
    'muhammad':['Osmondagi bolalar','Opa-singillar','Shaytanat'],
    'shavkat':['Vatan','Kichkina odamlar','Kechikkan hayot']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)