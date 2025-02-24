#########################
#Esercizi sui Moduli
def E1():
    print('-----------------------------')
    import math
    print(math.sqrt(16))
# end def
def E2():
    print('-----------------------------')
    import random
    print(random.randrange(1,10))
# end def
def E3():
    from numbers1 import somma
    print('-----------------------------')
    print(somma(9,2))
# end def
def E4():
    from numbers1 import lista_numeri
    print('-----------------------------')
    for x in lista_numeri:
        # comment: 
        print(x)
    # end for
#end def
def E5():
    import datetime
    print('-----------------------------')
    x = datetime.datetime.now()
    print(x)
def E6():
    from datetime import datetime
    print('-----------------------------')
    x = input("Please enter in 'gg/mm/aa/ format: ")
    x = datetime.strptime(x,'%d/%m/%y')
    print(x.strftime("%B"))
def E7():
    from datetime import datetime
    print('-----------------------------')
    x = input("Please enter in 'gg-mm-aa- format: ")
    x = datetime.strptime(x,'%d-%m-%Y')
    y = input("Please enter in 'gg-mm-aa- format: ")
    y = datetime.strptime(y,'%d-%m-%Y')
    print(abs(x-y).days)
# end def
def E8():
    import math
    print('-----------------------------')
    print(math.pow(2,3))
# end def
def E9():
    import math
    print('-----------------------------')
    print(math.sqrt(25))
# end def
def E10():
    import math
    print('-----------------------------')
    print(math.floor(5.80))
# end def
def E11():
    import math
    print('-----------------------------')
    print(math.ceil(5.80))
# end def
def E12():
    import math
    print('-----------------------------')
    print(math.factorial(12))
# end def
def E13():
    from datetime import datetime
    print('-----------------------------')
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
    print('-----------------------------')
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
    print('-----------------------------')
    print("numero random",random.randrange(0,6))
    print("numero random",random.randrange(5,10))
    print("numero random",random.randrange(0,10))
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