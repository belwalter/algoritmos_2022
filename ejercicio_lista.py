from lista import Lista





class Superhereo:

    def __init__(self, aparicion, nombre, casa, bio):
        self.aparicion = aparicion
        self.nombre = nombre
        self.casa = casa
        self.bio = bio
    
    def __str__(self):
        return f"{self.nombre} {self.aparicion}, {self.casa}"


heroes = [
    {'name': 'iron man', 'anio': 1961, 'casa': 'Marvel', 'bio': 'usa un traje de hierro'},
    {'name': 'batman', 'anio': 1975, 'casa': 'Dc', 'bio': '.....'},
    {'name': 'linterna verde', 'anio': 1979, 'casa': 'DC', 'bio': 'completar la bio'},
    {'name': 'capitan america', 'anio': 1973, 'casa': 'Marvel', 'bio': 'tiene un escudo de vibranio'},
    {'name': 'wolverine', 'anio': 1966, 'casa': 'Marvel', 'bio': 'pertenece a los x-men'},
    {'name': 'dr. strange', 'anio': 1970, 'casa': 'DC', 'bio': '.......'},
    {'name': 'mujer maravilla', 'anio': 1960, 'casa': 'DC', 'bio': '.......'},
    
]

lista_heroes = Lista()

for heroe in heroes:
    lista_heroes.insertar(Superhereo(heroe['anio'],
                                     heroe['name'].title(),
                                     heroe['casa'].capitalize(),
                                     heroe['bio']), 'nombre')


#! punto A
dato = lista_heroes.eliminar('linterna Verde'.title(), 'nombre')
if dato:
    print(f'el superheroes {dato.nombre} fue eliminado')
else:
    print('el superheroe no esta en la lista')

#! punto B
dato = lista_heroes.busqueda('wolverine'.title(), 'nombre')
if dato:
    print(f'el superheroe {dato.info.nombre} aparecieo en {dato.info.aparicion}')
else:
    print('el superheroe no esta en la lista')

#! punto C
dato = lista_heroes.busqueda('dr. strange'.title(), 'nombre')
if dato:
    dato.info.casa = 'Marvel'
    print(f'el superheroes {dato.info.nombre} fue modificado')
else:
    print('el superheroe no esta en la lista')


print()
lista_heroes.barrido()

#! punto D
print()
lista_heroes.barrido_armadura_traje()

#! punto E
print()
lista_heroes.barrido_anterior_1963()

#! punto F
print()
dato = lista_heroes.busqueda('mujer maravilla'.title(), 'nombre')
if dato:
    print(f'la {dato.info.nombre} pertenece a la casa {dato.info.casa}')
else:
    print('el superheroe no esta en la lista')
dato = lista_heroes.busqueda('capitana marvel'.title(), 'nombre')
if dato:
    print(f'la {dato.info.nombre} pertenece a la casa {dato.info.casa}')
else:
    print('el superheroe no esta en la lista')


print()
lista_heroes.barrido_comienza_con(['B', 'M', 'S'])

marvel, dc = lista_heroes.contar_por_casa()
print(f'cantidad de superheroes de Marvel {marvel} y de Dc {dc}')