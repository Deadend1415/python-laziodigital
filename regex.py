#########################
#Esercizi su i regEx
def e1():
    import re
    str1 = input("Please enter first string: ")
    str2 = input("Please enter last string: ")
    x = bool(re.search(r"a", str1 + str2))
    print(x)
# end def
def e2():
    import re
    x = re.sub("5", "cinque", "Hanno mangiato 5 mele e 5 arance")
    print(x)
# end def
def e3():
    import re
    x = re.sub(r"\s", "9", "Oggi è una bella giornata di sole.",count=1)
    print(x)
# end def
def e4():
    import re
    items = ['Gol', 'Giocatore', 'User', 'Sedia', 'Windows', 'Dado']
    print(x)
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