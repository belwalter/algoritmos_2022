from cola import Cola


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


def arbol_vacio():
    return arbol['info'] is None


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


def busqueda(arbol, clave):
    aux = None
    if arbol is not None and arbol['info'] is not None:
        if arbol['info'] == clave:
            aux = arbol
        elif clave < arbol['info']:
            aux = busqueda(arbol['izq'], clave)
        else:
            aux = busqueda(arbol['der'], clave)
    return aux


def remplazar(arbol, anterior=None, primero=None):
    aux = None
    if arbol['der'] is None:
        aux = arbol['info']
        if anterior:
            anterior['der'] = arbol['izq']
        else:
            primero['izq'] = arbol['izq']
    else:
        aux = remplazar(arbol['der'], anterior=arbol)
    return aux


def eliminar_nodo(arbol, clave):
    x = None
    if arbol['info'] is not None:
        if clave < arbol['info']:
            x = eliminar_nodo(arbol['izq'], clave)
        elif clave > arbol['info']:
            x = eliminar_nodo(arbol['der'], clave)
        else:
            x = arbol['info']
            if arbol['izq'] is None and arbol['der'] is not None:
                arbol['info'] = arbol['der']['info']
                arbol['izq'] = arbol['der']['izq']
                arbol['der'] = arbol['der']['der']
            elif arbol['der'] is None and arbol['izq'] is not None:
                arbol['info'] = arbol['izq']['info']
                arbol['der'] = arbol['izq']['der']
                arbol['izq'] = arbol['izq']['izq']
            else:
                aux = remplazar(arbol['izq'], primero=arbol)
                arbol['info'] = aux

    return x


def por_nivel(arbol):
    pendientes = Cola()
    pendientes.arribo(arbol)
    while not pendientes.cola_vacia():
        nodo = pendientes.atencion()
        print(nodo['info'])
        if nodo['izq']:
            pendientes.arribo(nodo['izq'])
        if nodo['der']:
            pendientes.arribo(nodo['der'])


arbol = nodoArbol()

insertar_nodo(arbol, 19)
insertar_nodo(arbol, 7)
insertar_nodo(arbol, 1)
insertar_nodo(arbol, 31)
insertar_nodo(arbol, 22)
insertar_nodo(arbol, 45)
insertar_nodo(arbol, 27)    
insertar_nodo(arbol, 24) 

# preorden(arbol)

# value = eliminar_nodo(arbol, 31)

# print('valor eliminado', value)

# preorden(arbol)

por_nivel(arbol)

# pos = busqueda(arbol, 45)
# if pos:
#     print('asdasd', pos['info'])

# postorden(arbol)