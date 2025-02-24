#########################
#Esercizi sui Moduli
def E1():
    import math
    print(math.sqrt(16))
# end def
def E2():
    import random
    print(random.randrange(1,10))
# end def
def E3():
    from numbers1_nuovo_modulo_ import somma
    print(somma(9,2))
# end def
def E4():
    from numbers1_nuovo_modulo_ import lista_numeri
    for x in lista_numeri:
        # comment: 
        print(x)
    # end for
#end def
def E5():
    import datetime
    x = datetime.datetime.now()
    print(x)
def E6():
    from datetime import datetime
    x = input("Please enter in 'gg/mm/aa/ format: ")
    x = datetime.strptime(x,'%d/%m/%y')
    print(x.strftime("%B"))
def E7():
    from datetime import datetime
    x = input("Please enter in 'gg-mm-aa- format: ")
    x = datetime.strptime(x,'%d-%m-%Y')
    y = input("Please enter in 'gg-mm-aa- format: ")
    y = datetime.strptime(y,'%d-%m-%Y')
    print(abs(x-y).days)
# end def
def E8():
    import math
    print(math.pow(2,3))
# end def
def E9():
    import math
    print(math.sqrt(25))
# end def
def E10():
    import math
    print(math.floor(5.80))
# end def
def E11():
    import math
    print(math.ceil(5.80))
# end def
def E12():
    import math
    print(math.factorial(12))
# end def
def E13():
    from datetime import datetime
    x = input("Please enter in 'gg-mm-aa format: ")
    x = datetime.strptime(x,'%d-%m-%Y')
    match(x.strftime("%a")):
        case ("Mon"):
            # comment: 
            print("Lunedi")
        case ("Tue"):
            # comment: 
            print("Martedi")
        case ("Wed"):
            # comment: 
            print("Mercoledi")
        case ("Thu"):
            # comment: 
            print("Giovedi")
        case ("Fri"):
            # comment: 
            print("Venerdi")
        case ("Sat"):
            # comment: 
            print("Sabato")
        case ("Sun"):
            # comment: 
            print("domenica")
# end def
def E14():
    import random
    lista= ["ciao", True, 25, "x"]
    dictionary = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964}
    res = random.choice(list(dictionary.items()))
    print("elemento random dalla lista:",random.choice(lista))
    print("elemento random dall dictionary:",res)
# end def
def E15():
    import random
    from datetime import datetime, timedelta
    print("numero random",random.randrange(0,6))
    print("numero random",random.randrange(5,10))
    print("numero random",random.randrange(0,10))
    #data randomica tra due intervalli ↓
    date1 = datetime(2020, 1, 1)
    date2 = datetime(2025, 12, 31)
    delta = date2 - date1
    random_days = random.randint(0, delta.days)

    # Generate the random date
    random_date = date1 + timedelta(days=random_days
    )
    print(random_date.date())
# end def
def E16():
    import random
    lista = [1,3,"x0","Dan"]
    print("before shuffle:",lista)
    random.shuffle(lista)   
    print(lista)
# end def
def E17():
    import random
    print("numereo tra 0 e 1 :",random.randrange(0,1))
    x = input("Input l'intervallo: ")
    y = input("Input l'intervallo: ")
    print("numereo tra 0 e 1 :",random.randrange(x,y))
# end def
def E18():
    import random
    new = []
    for i in range(random.randrange(10)):
        # comment: 
        new.append(random.randrange(10))
    # end for
    print(new,"Lunghezza: ",len(new))
# end def
def E19():
    import datetime
    x = datetime.datetime.now()
    print("Data e ora correnti",x)
    print("Anno concorrente",x.strftime("%Y"))
    print("Mese dell'anno",x.strftime("%B %Y"))
    print("Numero settimana dell anno",x.strftime("%W"))
    print("Giorno della settimana",x.strftime("%d"))
    print("Giorno dell'anno",x.strftime("%a %Y"))
    print("Giorno dell mese",x.strftime("%d"))
# end def
################### MAIN #######################
a=1 #variable for infinite loop
while (a != 0):
    # comment: 
    option = input("Please enter desired exercise number: ")
    match (option):
        case ('1'):
            # comment: 
            E1()
        case ('2'):
            # comment: 
            E2()
        case ('3'):
            # comment: 
            E3()
        case ('4'):
            # comment: 
            E4()
        case ('5'):
            # comment: 
            E5()
        case ('6'):
            # comment: 
            E6()
        case ('7'):
            # comment: 
            E7()
        case ('8'):
            # comment: 
            E8()
        case ('9'):
            # comment: 
            E9()
        case ('10'):
            # comment: 
            E10()
        case ('11'):
            # comment: 
            E11()
        case ('12'):
            # comment: 
            E12()
        case ('13'):
            # comment: 
            E13()
        case ('14'):
            # comment: 
            E14()
        case ('15'):
            # comment: 
            E15()
        case ('16'):
            # comment: 
            E16()
        case ('17'):
            # comment: 
            E17()
        case ('18'):
            # comment: 
            E18()
