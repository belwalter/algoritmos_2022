
def nodoArbol():
    nodo = {
        'info': None,
        'der': None,
        'izq': None,
    }
    return nodo


def insertar_nodo(arbol, dato):
    if arbol['info'] is None:
        arbol['info'] = dato
    elif dato < arbol['info']:
        if arbol['izq'] is None:
            arbol['izq'] = nodoArbol()
        insertar_nodo(arbol['izq'], dato)
    else:
        if arbol['der'] is None:
            arbol['der'] = nodoArbol()
        insertar_nodo(arbol['der'], dato)


def preorden(arbol):
    if(arbol is not None):
        print(arbol['info'])
        preorden(arbol['izq'])
        preorden(arbol['der'])


def inorden(arbol):
    if(arbol is not None):
        inorden(arbol['izq'])
        print(arbol['info'])
        inorden(arbol['der'])

def postorden(arbol):
    if(arbol is not None):
        postorden(arbol['der'])
        print(arbol['info'])
        postorden(arbol['izq'])


arbol = nodoArbol()

insertar_nodo(arbol, 19)
insertar_nodo(arbol, 7)
insertar_nodo(arbol, 11)
insertar_nodo(arbol, 31)
insertar_nodo(arbol, 22)
insertar_nodo(arbol, 45)
insertar_nodo(arbol, 27)    


postorden(arbol)