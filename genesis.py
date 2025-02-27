"""HI """
print("--------------------------------------------------------------------------")
#########################
# Esercizio sulle variabli
def Esercizio1():
    print("Esercizio sulle variabili" + "\n-----------------------------")
    nome = input("Input name ")
    print(nome)
#########################
# Esercizio sulle stringhe
def Esercizio2():
    print("Esercizio sulle stringhe" + "\n-----------------------------")
    stringa =  "Hello World!"
    print(stringa.upper())
# end def
def Esercizio3():
    print("\n-----------------------------")
    stringa = "il meglio deve ancora venire"
    print(stringa.split())
# end def
def Esercizio4():
    print("\n-----------------------------")
    stringa = " Ciao "
    print(stringa.strip())
# end def
#########################
# Esercizio sulle operazioni matematiche
def Esercizio5():
    print("Esercizio sulle operazioni matematiche " + "\n-----------------------------")
    numero = 4
    numero1 = 1
    numero2 = numero - numero1
    print(numero2)
# end def    
def Esercizio6():
    print("\n-----------------------------")
    numero = 4
    numero1 = 1
    numero2 = numero + numero1
    print(numero2)
#########################
# Esercizio su tipi di dato
def Esercizio7():
    print("Esercizio su tipi di dato " + "\n-----------------------------")
    numero = 4
    print(type(numero))
# end def    
def Esercizio8():
    print("Esercizio su tipi di dato " + "\n-----------------------------")
    numero_decimale = "float"
    print(type(numero_decimale))
#########################
# Esercizio condizionali
def Esercizio9():
    print("Esercizio condizionali " + "\n-----------------------------")
    x = int(input("Please enter: "))
    if (x > 0): 
        print("Il numero è positivo")
    else: 
        print("Il numero è negativo ")
    # end if
# end def
def Esercizio10():
    if (x > y):
        # comment:
        print("Il numero è maggiore") 
    elif (x == y):
        # comment: 
        print("I numeri sonon uguali")
    else:
        # comment: 
        print("Il secondo numero è maggiore")
    # end if
    
# end def