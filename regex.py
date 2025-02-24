#########################
#Esercizi su i regEx
def e1():
    import re
    str1 = input("Please enter first string: ")
    str2 = input("Please enter last string: ")
    x = bool(re.search("a", str1 + str2))
    print(x)
# end def

################### MAIN #######################
a=1 #variable for infinite loop
while (a != 0):
    # comment: 
    option = input("Please enter desired exercise number: ")
    match (option):
        case ('1'):
            # comment: 
            e1()