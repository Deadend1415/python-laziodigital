#########################
# Esercizi su i file
#########################
def e1():
    file = open("f1")
    print(file.read())
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