
from pila import Pila
from random import randint

pila1 = Pila()
pila_aux = Pila()

for i in range(10):
    num = randint(1, 100)
    print(num)
    pila1.apilar(num)

# ejercicio 1
# x = int(input('ingrese el numero que desae contar ocurrencias '))

# contador = 0
# while(not pila1.pila_vacia()):
#     dato = pila1.desapilar()

#     if(dato == x):
#         contador += 1

# print('cantidad de ocurrencias:', contador)

# ejercicio 2
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()

    if(dato % 2 == 0):
        pila_aux.apilar(dato)

while(not pila_aux.pila_vacia()):
    dato = pila_aux.desapilar()
    pila1.apilar(dato)

print('elementos pares')
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    print(dato)
