

def bernstein(cadena, size):
    h = 0
    cadena = cadena[:2]
    for caracter in cadena:
        h = h * 33 + ord(caracter)
    
    return h % size


def hash_numerico(cadena):
    numero = int(cadena[3:])
    return numero


def generar_stormtrooper():
    from random import randint, choice
    legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO', 'CA']

    stormtrooper = choice(legiones)+str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))+str(randint(0, 9))
    return stormtrooper


tabla_hash_legion = [None] * 15
tabla_hash_numerica = [None] * 1000


for i in range(20000):
    trooper = generar_stormtrooper()
    posicion = bernstein(trooper, len(tabla_hash_legion))
    if(not tabla_hash_legion[posicion]):
        tabla_hash_legion[posicion] = []
    tabla_hash_legion[posicion].append(trooper)
    posicion = hash_numerico(trooper)
    if(not tabla_hash_numerica[posicion]):
        tabla_hash_numerica[posicion] = []
    tabla_hash_numerica[posicion].append(trooper)

# for index, lista in enumerate(tabla_hash_numerica):
#     if(lista):
#         print(index, lista)

# for lista in tabla_hash_legion:
#     print(lista)

#! punto C
trooper = 'FN2187'

tabla_hash_numerica[187].append(trooper)
posicion2 = bernstein('FN', len(tabla_hash_legion))
tabla_hash_legion[posicion2].append(trooper)

posicion = hash_numerico(trooper)
if(tabla_hash_numerica[posicion] and trooper in tabla_hash_numerica[posicion]):
    print(f'el troper {trooper} esta en la lista')
    tabla_hash_numerica[posicion].remove(trooper)
    tabla_hash_legion[posicion2].remove(trooper)

else:
    print(f'el troper {trooper} no esta en la lista')
print(tabla_hash_numerica[posicion])


#! d
print()
print(tabla_hash_numerica[781])
print()
print(tabla_hash_numerica[537])

#! e
# print()
# posicion = bernstein('CT', len(tabla_hash_legion))
# print(tabla_hash_legion[posicion])
# print()
posicion = bernstein('FN', len(tabla_hash_legion))
print(tabla_hash_legion[posicion])
print(len(tabla_hash_legion[posicion]))