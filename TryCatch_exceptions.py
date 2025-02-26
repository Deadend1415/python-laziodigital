#########################
# Esercizi Try and exceprions
def e1():
    try:
        divisione= 50/0
    except ZeroDivisionError:
        print("non si può dividere per zero")
    else:
        print(divisione)
    # end try
# end def
def e2():
    try:
        x = int(input("Please enter: "))
        print(x)
    except ValueError:
        print("non è un numero")
    else:
        print(x)
    # end try
# end def
def e3():
    try:
        file = open("filename.txt")#apre in read
    except FileNotFoundError :
        print("File non esiste")
    # end try
# end def
def e4():
    try:
        x = int(input("Please enter: "))
        y = input("Please enter: ")
        print(x+y)
    except TypeError:
        print("le due variabili non sono dello stesso tipo")
    # end try
# end def
def e6():
    try:
        x = int(input("Please enter: "))
        list = ["dan","mike"]
        print(list[x])
    except IndexError:
        print("Non esiste quel indice")
    # end try
# end def
def e7():
    try:
        y = input("Please enter: ")
    except KeyboardInterrupt:
        print("Operazione cancellata")
    else:
        print(y)
    # end try
# end def
def e8():
    try:
        list = ("dan","mike")
        list.append("item")
    except AttributeError:
        print("Metodo non è presente per le tuple")
    # end try
# end def

################### MAIN #######################
a=1 #variable for infinite loop
while (a != 0):
    # comment: 
    option = input("Please enter desired exercise number: ")
    print('-----------------------------')
    match (option):
        case ('1'):
            # comment: 
            e1()
        case ('2'):
            # comment: 
            e2()
        case ('3'):
            # comment: 
            e3()
        case ('4'):
            # comment: 
            e4()
        case ('6'):
            # comment: 
            e6()
        case ('7'):
            # comment: 
            e7()
        case ('8'):
            # comment: 
            e8()
    print('-----------------------------')
#end while