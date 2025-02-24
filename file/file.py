#########################
# Esercizi su i file
#########################
def e1():
    file = open("./file/f1")
    print(file.read())
# end def
def e2():
    ans = input("Please enter: ")
    file = open("./file/f1","a")
    file.write(ans)
    file.close()
    print("Inputted: ",ans)
# end 
def e3():
    file = open("./file/f1")
    x = file.read()
    print("Copying :",x) 
    file2 = open("./file/f1_copy","w")
    file2.write(x)
    file2.close()
# end def
def e4():
    import json
    x = {"nome": "Mario", "cognome": "Rossi", "eta":25, "email":"something@gmail.com", "number":+39}
    print(json.dumps(x))
# end def
def e5():
    list = []
    file = open("./file/f3")
    for i in file:
        # comment:
         list.append(i)
    # end for
    print(list)
# end def
def e6():
    import json
    #Aggiunto users al file json la prima volta
    # users = {"001": "Marco", "002": "Monica", "003": "Giovanni"}
    #f = open("./file/f4.json","a")
    #f.write(json.dumps(users))
    dict = {"004":"Giulia","005":"Giacomo","006":"Lusia"}
    file = open("./file/f4.json", "r+")
    dati= json.load(file)
    dati.update(dict)
    # riposiziono il cursone all'inizio del file:
    file.seek(0)

    #inserisco tutto nel file:

    json.dump(dati, file)

    file.close()
# end def
def e7():
    f = open(".file/f3")
    x = input("Please enter range: ")
    for i in range(x):
        print(f.readline())
    # end for
# end def
def e8():
    file = open("./file/f1")
    print("Before append :",file.read())
    file.close()
    ans = input("Please enter: ")
    file = open("./file/f1","a")
    file.write(ans + "\n")
    file.close()
    file = open("./file/f1")
    print("After append :",file.read())
    file.close()
    # end for
# end def
def e10():
    list = []
    file = open("./file/f5","w")
    for i in list:
        # comment: 
        file.write(i + "\n")
    # end for
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
        case ('5'):
            # comment: 
            e5()
        case ('6'):
            # comment: 
            e6()
        case ('7'):
            # comment: 
            e7()
        case ('8'):
            # comment: 
            e8()
        case ('9'):
            # comment: 
            e9()
    print('-----------------------------')
#end while