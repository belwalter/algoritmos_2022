def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoArista():
    info, sig, peso = None, None, None
    #? info es el destino


class nodoVertice():
    info, sig, visitado, adyacentes = None, None, False, None


class Arista():
    
    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar_arista(self, dato, peso, campo=None):
        #! si el grafo es no dirigido doble insercion
        nodo = nodoArista()
        nodo.info = dato
        nodo.peso = peso

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def tamanio(self):
        return self.__tamanio

    def barrido_aristas(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
    def busqueda_arista(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
        if dato:
            self.__tamanio -= 1 

        #! eliminar arista destino origen
        return dato

    def obtener_elemento_vertice(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None


class Grafo():

    def __init__(self, dirigido=True):
        self.__inicio = None
        self.__tamanio = 0
        self.__dirigido = dirigido


    def insertar_vertice(self, dato, campo=None):
        nodo = nodoVertice()
        nodo.info = dato
        nodo.adyacentes = Arista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def tamanio(self):
        return self.__tamanio

    def barrido_vertice(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
#     def barrido_lista_lista(self):
#         aux = self.__inicio
#         while(aux is not None):
#             print(aux.info)
#             print('sublista:')
#             aux.sublista.barrido()
#             # aux1 = aux.sublista.__inicio
#             # while(aux1 is not None):
#             #     print('  ', aux1.info)
#             #     aux1 = aux1.sig

#             aux = aux.sig

    def busqueda_vertice(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
        if dato:
            self.__tamanio -= 1 

        #! eliminar todas las aristas que apuntan al vertice
        return dato

    def obtener_elemento_vertice(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None

#! barrido profundidad y amplitud
#! algoritmos especiales dijkstra prim kruskal

g = Grafo()

g.insertar_vertice('A')
g.insertar_vertice('Z')
g.insertar_vertice('F')
g.insertar_vertice('C')

g.barrido_vertice()