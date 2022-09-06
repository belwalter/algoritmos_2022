

class Heap():

    def __init__(self):
        self.vector = []
        self.tamanio = 0
    
    def agregar(self, dato):
        self.vector.insert(self.tamanio, dato)
        self.flotar(self.tamanio)
        self.tamanio += 1
    
    def flotar(self, indice):
        padre = (indice -1) // 2
        while(indice > 0 and self.vector[indice] > self.vector[padre]):
            self.vector[indice], self.vector[padre] = self.vector[padre], self.vector[indice]
            indice = padre
            padre = (indice -1) // 2
    
    def quitar(self):
        x = self.vector[0]
        self.vector[0], self.vector[self.tamanio-1] = self.vector[self.tamanio-1], self.vector[0]
        #hundir(0)
        self.vector.pop()
        self.tamanio -= 1
        return x


h = Heap()

h.agregar(1)
h.agregar(2)
h.agregar(3)
h.agregar(4)
h.agregar(5)
h.agregar(3)
print(h.vector, h.tamanio)
print('elemento eliminado:', h.quitar(), h.tamanio)
print('elemento eliminado:', h.quitar(), h.tamanio)
print(h.vector)
a = input()
h.agregar(10)
print(h.vector)
print('elemento eliminado:', h.quitar(), h.tamanio)
print(h.vector)