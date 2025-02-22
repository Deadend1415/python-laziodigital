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

E13()