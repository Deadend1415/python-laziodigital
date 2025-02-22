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
    from numbers1 import somma
    print(somma(9,2))
# end def
def E4():
    from numbers1 import lista_numeri
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
    x = input("Please enter in 'gg/mm/aa/ format: ")
    x = datetime.strptime(x,'%d-%m-%Y')
    print(x.strftime("%a"))

a=1 #variable for infinite loop
while (a != 0):
    # comment: 
    option = input("Please enter: ")
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