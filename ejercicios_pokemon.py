from lista import Lista
from random import randint, choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
    
    def __str__(self):
        return self.nombre

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} - {self.nivel}"

lista_entrenadores = Lista()

enternadores = [
    {'name': 'uno', 'tg': 15, 'bg': 45,  'bp': 11},
    {'name': 'dos', 'tg': 3, 'bg': 12,  'bp': 35},
    {'name': 'tres', 'tg': 0, 'bg': 50,  'bp': 50},
    {'name': 'cuatro', 'tg': 1, 'bg': 10,  'bp': 1},
    {'name': 'cinco', 'tg': 7, 'bg': 25, 'bp': 8},
]

pokemons = [
    {'name': 'pok1', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'pok2', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'pok3', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
    {'name': 'pok4', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
    {'name': 'pok5', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'pok6', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]


for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],
                                           entrenador['tg'],
                                           entrenador['bp'],
                                           entrenador['bg']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],
                                      pokemon['nivel'],
                                      pokemon['tipo'],
                                      pokemon['subtipo']), 'nombre')

lista_entrenadores.barrido_lista_lista() 
print()   


#! punto a cantidad de pok de un entrenador
# entrenador = input('ingrese nombre del entrenador ')
# pos = lista_entrenadores.busqueda(entrenador, 'nombre')
# if(pos):
#     print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
# else:
#     print('el entrenador no esta en la lista')
# print()

#! entrenadores con mas de tres torneos
lista_entrenadores.barrido_entrenador_mas_tres()
print()
#! c
mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
print(mayor.info, mayor.sublista.mayor_de_lista('nivel').info)
print()

#! d
entrenador = input('ingrese nombre del entrenador ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"el entrenador tiene {pos.info}")
    print('sus pokemons')
    pos.sublista.barrido()
else:
    print('el entrenador no esta en la lista')
print()

#! punto e
lista_entrenadores.barrido_porcentaje_victorias()