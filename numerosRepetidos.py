

def numRep(lista):
    diccionario = {}
    for x in lista:
        if type(x) == str:
            return "La lista solo puede contener numeros"
    for i in lista:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario
