
from pila import Pila
from random import randint

pila1 = Pila()
pila_invertida = Pila()
pila_2 = Pila()


# ! palindromo

# palabra = input('ingrese un palabra ')

# for letra in palabra:
#     pila1.apilar(letra)


# while(not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     pila_invertida.apilar(dato)
#     pila_2.apilar(dato)


# while(not pila_2.pila_vacia()):
#     pila1.apilar(pila_2.desapilar())


# while(not pila1.pila_vacia() and (pila1.cima() == pila_invertida.cima())):
#     pila1.desapilar()
#     pila_invertida.desapilar()

# if(pila1.pila_vacia()):
#     print('la palabra es un palindromo')
# else:
#     print('no es un palindromo', pila1.tamanio())





# print(pila1)

# for i in range(10):
#     num = randint(1, 100)
#     print(num)
#     pila1.apilar(num)

# ejercicio 1
# x = int(input('ingrese el numero que desae contar ocurrencias '))

# contador = 0
# while(not pila1.pila_vacia()):
#     dato = pila1.desapilar()

#     if(dato == x):
#         contador += 1

# print('cantidad de ocurrencias:', contador)

# ejercicio 2
# while(not pila1.pila_vacia()):
#     dato = pila1.desapilar()

#     if(dato % 2 == 0):
#         pila_aux.apilar(dato)

# while(not pila_aux.pila_vacia()):
#     dato = pila_aux.desapilar()
#     pila1.apilar(dato)

# print('elementos pares')
# while(not pila1.pila_vacia()):
#     dato = pila1.desapilar()
#     print(dato)

# def random_character():
#     from random import randint
#     return chr(randint(65, 90)) #! mayuscula
# #     # return chr(randint(97, 122)) #! minuscula

# for i in range(15):
#     caracter = random_character() 
#     print(caracter)
#     pila1.apilar(caracter)

# contador = 0
# while(not pila1.pila_vacia()):
#     caracter = pila1.desapilar()
#     if(caracter in ['A', 'E', 'I', 'O', 'U']):
#         contador += 1

class Traje():
    traje, pelicula, estado = None, None, None

dic = {'traje': 'Mark1', 'pelicula': 'dasdsa', 'estado': 'asdads'}

dic['traje']

# print('cantidad de vocales', contador)
trajes = ['Mark LXXXV', 'Mark II', 'Mark IV', 'Mark V', 'Mark X', 'Mark XLIV']
peliculas = ['iron man I', 'iron man II','iron man III', 'Avengers1', 'Spider-Man: Homecoming', 'Capitan America: Civil War']
estado = ['Dañado', 'Impecable', 'Destruido']

from random import choice

for i in range(len(trajes)):
    dato = Traje()
    dato.traje = trajes[i]
    dato.pelicula = peliculas[i]
    dato.estado = choice(estado)
    dic = {'traje': trajes[i], 'pelicula': peliculas[i], 'estado': choice(estado)}
    print(dato.traje, dato.pelicula, dato.estado)
    pila1.apilar(dato)

print()
pelicula = input('ingrese la pelicula en la que se uso el traje Mark LXXXV ')
insertar = True
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    # !A
    if(dato.traje == 'Mark XLIV'):
        print('el traje Mark XLIV fue usado en la pelicula', dato.pelicula)
    # !B
    if(dato.estado == 'Dañado'):
        print(f'el modelo {dato.traje} resulto dañado')
    # print(dato.traje, dato.pelicula, dato.estado)
    # !F
    if(dato.pelicula in ['Spider-Man: Homecoming', 'Capitan America: Civil War']):
        print(f'el modelo {dato.traje} fue utilizado en la pelicula {dato.pelicula}')
    # !E
    if(dato.traje == 'Mark LXXXV' and dato.pelicula == pelicula):
        insertar = False
    if(dato.estado != 'Destruido'):
        pila_2.apilar(dato)

while(not pila_2.pila_vacia()):
    pila1.apilar(pila_2.desapilar())

if(insertar):
    dato = Traje()
    dato.traje = 'Mark LXXXV'
    dato.pelicula = pelicula
    dato.estado = choice(estado)
    pila1.apilar(dato)

print()
while(not pila1.pila_vacia()):
    dato = pila1.desapilar()
    print(dato.traje, dato.pelicula, dato.estado)