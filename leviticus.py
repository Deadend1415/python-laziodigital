###############
# Esercizi sulle Funzioni
def Esercizio1(x):
    print("---------------------")
    somma = 0
    list = x
    for i in list:
        # comment: 
        somma += list[i-1]
    # end for
    print(somma)
# end def
def Esercizio2(x):
    print("---------------------")
    print(x[::-1])
# end def
def Esercizio3(x):
    print("---------------------")
    new = []
    for i in x:
        # comment: 
        if i.startswith("a"):
            # comment: 
            new.append(i)
        # end if
    # end for
    return new
def Esercizio4(x):
    print("---------------------")
    new = []
    for i in x:
        # comment: 
        if (x[i] % 2 == 0):
            # comment: 
            new.append(i)
        # end if
    # end for
    return new
# end def
Esercizio3(x = ["ar","dr","as"])