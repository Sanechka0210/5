import stdiomask
alf="abcdefghijklmnopqrstuvwxyz"
one=input("Введите первое слово: ")
two=input("Введите второе слово: ")
three=input("Введите третье слово: ")
passw=""
passw+=alf[(alf.index(three[0]) + 1)]
passw+=alf[(alf.index(three[0]) + 2)]
passw+=alf[(alf.index(two[2]) - 1)]
if len(three)% 2 != 0:
    passw+=alf[(alf.index(three[3]) -1)]
else:
    if alf.index(three[len(three)//2])>alf.index(three[len(three)//2 -1]):
        passw+=alf[(alf.index(three[len(three)//2]) - 1)]
    else:
        passw+=alf[(alf.index(three[len(three)//2 -1]) - 1)]
if (len(one)+len(two))> 26:    
    passw+=alf[(((len(one)+len(two))-1)) % 26]
else:
    passw+=alf[(len(one)+len(two))-1]
print(passw)
userPassw=stdiomask.getpass()
if userPassw==passw:
    print("Пароль верный")
else:
    print("Пароль неверный")
