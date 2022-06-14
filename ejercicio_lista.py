from lista import Lista


# class Superhereo:

#     def __init__(self, aparicion, nombre, casa, bio):
#         self.aparicion = aparicion
#         self.nombre = nombre
#         self.casa = casa
#         self.bio = bio

#     def __str__(self):
#         return f"{self.nombre} {self.aparicion}, {self.casa}"


# heroes = [
#     {'name': 'iron man', 'anio': 1961, 'casa': 'Marvel', 'bio': 'usa un traje de hierro'},
#     {'name': 'batman', 'anio': 1975, 'casa': 'Dc', 'bio': '.....'},
#     {'name': 'linterna verde', 'anio': 1979, 'casa': 'DC', 'bio': 'completar la bio'},
#     {'name': 'capitan america', 'anio': 1973, 'casa': 'Marvel', 'bio': 'tiene un escudo de vibranio'},
#     {'name': 'wolverine', 'anio': 1966, 'casa': 'Marvel', 'bio': 'pertenece a los x-men'},
#     {'name': 'dr. strange', 'anio': 1970, 'casa': 'DC', 'bio': '.......'},
#     {'name': 'mujer maravilla', 'anio': 1960, 'casa': 'DC', 'bio': '.......'},

# ]

# lista_heroes = Lista()

# for heroe in heroes:
#     lista_heroes.insertar(Superhereo(heroe['anio'],
#                                      heroe['name'].title(),
#                                      heroe['casa'].capitalize(),
#                                      heroe['bio']), 'nombre')


# #! punto A
# dato = lista_heroes.eliminar('linterna Verde'.title(), 'nombre')
# if dato:
#     print(f'el superheroes {dato.nombre} fue eliminado')
# else:
#     print('el superheroe no esta en la lista')

# #! punto B
# dato = lista_heroes.busqueda('wolverine'.title(), 'nombre')
# if dato:
#     print(f'el superheroe {dato.info.nombre} aparecieo en {dato.info.aparicion}')
# else:
#     print('el superheroe no esta en la lista')

# #! punto C
# dato = lista_heroes.busqueda('dr. strange'.title(), 'nombre')
# if dato:
#     dato.info.casa = 'Marvel'
#     print(f'el superheroes {dato.info.nombre} fue modificado')
# else:
#     print('el superheroe no esta en la lista')


# print()
# lista_heroes.barrido()

# #! punto D
# print()
# lista_heroes.barrido_armadura_traje()

# #! punto E
# print()
# lista_heroes.barrido_anterior_1963()

# #! punto F
# print()
# dato = lista_heroes.busqueda('mujer maravilla'.title(), 'nombre')
# if dato:
#     print(f'la {dato.info.nombre} pertenece a la casa {dato.info.casa}')
# else:
#     print('el superheroe no esta en la lista')
# dato = lista_heroes.busqueda('capitana marvel'.title(), 'nombre')
# if dato:
#     print(f'la {dato.info.nombre} pertenece a la casa {dato.info.casa}')
# else:
#     print('el superheroe no esta en la lista')


# print()
# lista_heroes.barrido_comienza_con(['B', 'M', 'S'])

# marvel, dc = lista_heroes.contar_por_casa()
# print(f'cantidad de superheroes de Marvel {marvel} y de Dc {dc}')

class Jedi:

    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"


lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('jedis.txt')
lineas = file.readlines()


lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    # datos.pop(-1)
    lista_jedi.insertar(Jedi(datos[0],
                             datos[2],
                             datos[3].split('/'),
                             datos[4].split('/')),
                        campo='nombre')
    lista_jedi2.insertar(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),
                         campo='especie')
    # lista.append(Jedi(datos[0],
    #                   datos[2],
    #                   datos[3].split('/'),
    #                   datos[4].split('/')))
# !
lista_jedi.barrido()
print()
# lista_jedi2.barrido()

dato = lista_jedi.busqueda('kit fisto', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')

print()
lista_jedi.barrido_jedi_master()

print()
lista_jedi.barrido_comienza_con(['a'])

# def citerio(item):
#     return item.nombre + item.especie


# lista.sort(key=citerio)

# for jedi in lista:
#     print(jedi)

