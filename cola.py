

class nodoCola():
    info, sig = None, None


class Cola():

    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__tamnio = 0
    
    def arribo(self, dato):
        nodo = nodoCola()
        nodo.info = dato

        if self.__final is None:
            self.__frente = nodo
        else:
            self.__final.sig = nodo
        self.__final = nodo

        self.__tamnio += 1

    def atencion(self):
        dato = self.__frente.info

        self.__frente = self.__frente.sig
        if self.__frente is None:
            self.__final = None


        self.__tamnio -= 1
        return dato



    def tamanio(self):
        return self.__tamnio


c = Cola()
c.arribo(1)
c.arribo(2)
print('tamanio', c.tamanio())
print(c.atencion())
print('tamanio', c.tamanio())
print(c.atencion())
print('tamanio', c.tamanio())
c.arribo(3)
print('tamanio', c.tamanio())
print(c.atencion())