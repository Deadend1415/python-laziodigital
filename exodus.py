########################
# Esercizio sulle tuple
global_collecion = tuple(("mela","banana","kiwi"))
global_dictionary = {
        "nome" : "Mario",
        "cognome" : "Rossi",
        "età" : 30
    }
def Esercizio1():
    print("-----------------------------")
    collection = tuple(())
    print(type(collection))
# end def
def Esercizio2():
    print("-----------------------------")
    collecion = tuple(("mela","banana","kiwi"))
    print(collecion)
# end def
def Esercizio3():
    print("-----------------------------")
    print(global_collecion[1])
# end def
def Esercizio4():
    print("-----------------------------")
    new = global_collecion[0:2]
    print(new)
# end def
def Esercizio5():
    print("-----------------------------")
    if (global_collecion.count("mela") > 0):
        # comment: 
        print("Trovato!")
    else:
        # comment: 
        print("Assente")
    # end if
# end def
def Esercizio6():
    print("-----------------------------")
    print(len(global_collecion))
# end def
def Esercizio7():
    print("-----------------------------")
    tupla2 = ("pesca" , "arancia")
    new = global_collecion + tupla2
    print(new)
# end def
#########################
# Esercizi su set
def Esercizio8():
    print('-----------------------------')
    new = set(())
    print(type(new))
# end def
def Esercizio9():
    print('-----------------------------')
    new = {"mela","banana","kiwi","mela"}
    print(new)
# end def
#########################
# Esercizi Dictionary
def Esercizio10():
    print('-----------------------------')
    new = {}
    print(type(new))
# end def
def Esercizio11():
    new = {
        "nome" : "Mario",
        "cognome" : "Rossi",
        "età" : 30
    }
    print(new)
# end def
def Esercizioni12():
    print(global_dictionary["età"])
# end def
def Esercizioni13():
    dictionary = global_dictionary
    dictionary["email"] = "mario.rossi@email.com"
    print(global_dictionary)
# end def
def Esercizioni14():
    dictionary = global_dictionary.keys()
    print(dictionary)
# end def

######################### MAIN #############################
while (global_collecion != 0):
    # comment: 
    option = input("Please enter: ")
    match (option):
        case ('1'):
            # comment:
            Esercizio1() 
        case ('2'):
            # comment: 
            Esercizio2()
        case ('3'):
            # comment: 
            Esercizio3()
        case ('4'):
            # comment: 
            Esercizio4()
        case ('5'):
            # comment: 
            Esercizio5()
        case ('6'):
            # comment: 
            Esercizio6()
        case ('7'):
            # comment: 
            Esercizio7()
        case ('8'):
            # comment: 
            Esercizio8()
        case ('9'):
            # comment: 
            Esercizio9()
        case ('10'):
            # comment: 
            Esercizio10()
        case ('11'):
            # comment: 
            Esercizio11()
    # end match 
        case ('12'):
            # comment: 
            Esercizio12()
    # end match 
        case ('13'):
            # comment: 
            Esercizio13()
    # end match 
        case ('14'):
            # comment: 
            Esercizio14()
    # end match 
# end while