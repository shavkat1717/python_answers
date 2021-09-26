users = ['alisher1983','aziza','yasina', 'umar','shavkat1717']
login = input("Dear user! Please enter login: \t => ")
if login in users:
    print('This login already has chosen, please enter another login!')
else:
    print("Welcome to ", login, " !")