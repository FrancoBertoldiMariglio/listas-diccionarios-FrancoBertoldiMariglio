

class numRep():

    def __init__(self, lista):
        self.lista = lista

    def checkValid(self):
        for x in self.lista:
            if type(x) == str:
                return "La lista solo puede contener numeros"

    def rep(self):
        diccionario = {}
        for i in self.lista:
            if i in diccionario:
                diccionario[i] += 1
            else:
                diccionario[i] = 1
        return diccionario
