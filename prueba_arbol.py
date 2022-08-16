from arbol import (
    nodoArbol,
    insertar_nodo,
    inorden_villano,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden_heroes,
)

arbol = nodoArbol()


lista = [
    ['iron man', False],
    ['capiana marvel', False],
    ['thor', False],
    ['dotor strange', False],
    ['thanos', True],
    ['red skull', True],
    ['capitan america', False],
]

for nombre, villano in lista:
    insertar_nodo(arbol, nombre, villano)



inorden_villano(arbol)
print()
inorden_empieza_con(arbol, 'c')
print()
print(contar_heroes(arbol))

# clave = input('ingrese parte de lo que desea buscar ')
# inorden_empieza_con(arbol, clave)
# print()
# clave = input('ingrese nombre que desea modificar ')
# pos = eliminar_nodo(arbol, clave)
# if pos:
#     name = input('ingrese nuevo nombre ')
#     insertar_nodo(arbol, name, False)
# else:
#     print('valor no encontrado en el arbol')

# inorden(arbol)
print()

postorden_heroes(arbol)