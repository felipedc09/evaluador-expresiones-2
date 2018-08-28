from pila import *
from arbol import *
from utilidades import readLinesFile, writeInFile, appendInFile

variables = []


def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0], nodo_izq, nodo_der))
        else:
            if lista[0].isalpha():
                if len(lista) == 1:
                    agregarVariable(lista[0], evaluar(pila.desapilar()))
                else:
                    pila.apilar(Nodo(obtenerVariable(lista[0])))
            else:
                pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:], pila)


def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)


def agregarVariable(clave, valor):
    indexClave = -1
    if len(variables) != 0:
        for indice in range(len(variables)):
            if clave == variables[indice][0]:
                indexClave = indice
        if indexClave == -1:
            variables.append([clave, valor])
        else:
            variables[indexClave] = [clave, valor]
    else:
        variables.append([clave, valor])


def obtenerVariable(clave):
    valor = -1
    for variable in variables:
        if variable[0] == clave:
            valor = variable[1]
    if valor == -1:
        print("No esta asignada la variable: " + clave)
    else:
        return valor


writeInFile('expresiones.out', "Expresiones")

for exp in readLinesFile('expresiones.in'):
    listExp = exp.strip('\n').split(' ')
    # print(listExp)
    pila = Pila()
    convertir(listExp, pila)
    appendInFile('expresiones.out', str(listExp))    

appendInFile('expresiones.out', "Resultados")
appendInFile('expresiones.out', str(variables))
