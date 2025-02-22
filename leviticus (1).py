###############
# Esercizi sulle Funzioni
def Esercizio1(x):
    print("---------------------")
    somma = 0
    list = x
    for i in list:
        # comment: 
        somma += list[i-1]
    # end for
    print(somma)
# end def
def Esercizio2(x):
    print("---------------------")
    print(x[::-1])
# end def
def Esercizio3(x):
    print("---------------------")
    new = []
    for i in x:
        # comment: 
        if i.startswith("a"):
            # comment: 
            new.append(i)
        # end if
    # end for
    return new
def Esercizio4(x):
    print("---------------------")
    new = []
    for i in x:
        # comment: 
        if (x[i] % 2 == 0):
            # comment: 
            new.append(i)
        # end if
    # end for
    return new
# end def
def Esercizio5(x):
    return len(x)
# end def
def Esercizio6_7(x):
    """ Senza funzione built-in
    max = 0
    for i in x:
        # comment: 
        if (i > max):
            # comment:
            max = i 
        # end if
    # end for """
    print(max(x))
# end def Esercizio 6 e 7
def Esercizio8(x):
    print(sum(x)/len(x))
# end def
def Esercizio9(x):
    directory = {}
    for i in x:
        # comment:
        directory.update({i:x.count(i)}) 
    # end for
    print(directory)
# end def
def Esercizio10(x):
    directory = {"numero":x,"iarde":x * 9.14,"piedi e pollici":x * 3.28,"miglio terrestre": x / 1609.34}
    print(directory)
# end def
#########################
# Esercizi funzioni Lambda
def Esercizio11():
    x = lambda a : a * a
    print(x(5))
# end def
def Esercizio12(x):
    lista = list(map(lambda a: a * 2,x))
    print(lista)
# end def
def Esercizio13(x):
    lista = list(filter(lambda x: x.startswith("c"), x))
    print(lista)
# end def
def Esercizio14():
    x = lambda a , b: a * a + b * b
    print(x(5,4))
# end def
#########################
# Esercizi su le classi 
def Esercizio15():
    class persona:
        # instance attribute
        def __init__(self, name, age,sex):
            self.name = name
            self.age = age
            self.sex = sex
        def presentati(self):
            print(f"Ciao, mi chiamo {self.name},Sono {self.sex} e ho {self.age} anni")
    
    p1=persona("Daniel","20","Maschio")
    p1.presentati()
# end def
def Esercizio16():
    class Animali:
        def __init__(self, nome, specie, verso):
            self.nome = nome
            self.specie = specie
            self.verso = verso
        # end def
        def emettiSuono(self):
            print(self.verso)
        #end def
    # end class
    gatto = Animali("gatto","ragdoll","Meow")
    cane = Animali("cane","dobberman","Bow!")
    gatto.emettiSuono()
    cane.emettiSuono()
#end def
def Esercizio17():
    class Macchina:
        def __init__(self, marca, modello, anno):
            self.marca  = marca
            self.modello = modello
            self.anno = anno
        # end def
        def Descrizione(self):
            print(f"Questa è una {self.marca} {self.modello} dell'anno {self.anno}")
        #end def
    # end class
    ToyotaCamri = Macchina("Toyota","Camri",2030)
    ToyotaCamri.Descrizione()
#end def
def Esercizio18():
    class Cibo:
        def __init__(self, peso,nome):
            self.nome = nome            
            self.__peso = peso
        # end alternate constructor
        def nome(self):
            print(self.name)
        # end def
        def getPeso(self):
            print(self.__peso)
        # end def
    # end class
    class Deriv_animale(Cibo):
        def __init__(self, name, peso, nomeAnimale):
            super().__init__(name, peso)
            self.nomeAnimale = nomeAnimale
    class Deriv_vegetale(Cibo):
        def __init__(self, name, peso, colore):
            super().__init__(name, peso)
            self.colore = colore
# end def