mail = "semhodnekrasnej10@gmail.com"
for znak in range(len(mail)): #tady určít, že znak = cokoliv, v range(délky mailu, čož = 23 znaků)
    if mail[znak] ==".":    #tady if statement, pokud v mail[znak] (což je seznam) je ".", tak cčko = znak a vytiskne to c
        c=znak
        print("Tvoja doména je:",mail[c:])
for znak in range(len(mail)): #viz výše, určitě by to šlo udělat do 1dné f-ce for, ale takhle ti to funguje, tak to nech
    if mail[znak] =="@":
        c=znak
        d= mail.find(".") #tady jsem dal f-ci mail.find před 1. print, abych mohl printnout vše co je mezi "@" a "."
        print("Tvoj server je:",mail[c+1:d]) #viz výše, print všeho mezi @ a .
        print(d) #asi v zadání?
        print("Meno používateľa:",mail[:c])
