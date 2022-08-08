from jurassic_park import dinosaurs
from lista import Lista
from cola import Cola

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name'], dino['type']


class Dinosaurio:
    def __init__(self, fecha, codigo, nombre, level, type):
        self.nombre = nombre
        self.fecha = fecha
        self.codigo = codigo
        self.level = level
        self.type = type

    def __str__(self):
        return f"{self.fecha} - {self.nombre} - {self.codigo} - {self.level} - {self.type}"

lista_fecha = Lista()
lista_nombre = Lista()
cola_c = Cola()
cola_h = Cola()

file = open('alerts.txt')

lineas = file.readlines()
lineas.pop(0)

for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    name, type = busqueda(dato[2])
    dino = Dinosaurio(dato[0], dato[1], name, dato[3], type)
    lista_fecha.insertar(dino, 'fecha')
    lista_nombre.insertar(dino, 'nombre')
    if(dino.level in ['critical', 'high']):
        if(dino.type == 'carnívoro '):
            cola_c.arribo(dino)
        else:
            cola_h.arribo(dino)

lista_fecha.barrido()
print()
lista_nombre.barrido()

zonas = ['WYG075', 'SXH966', 'LYF010']

for code in zonas:
    dato = lista_fecha.eliminar(code, 'codigo')
    if dato:
        print(f'zona {dato} eliminada de la lista fecha')
    dato = lista_nombre.eliminar(code, 'codigo')
    if dato:
        print(f'zona {dato} eliminada de la lista nombre')


pos = lista_fecha.busqueda('HYD195', 'codigo')
if pos:
    pos.info.nombre = 'nuevo nombre'

pos = lista_nombre.busqueda('HYD195', 'codigo')
if pos:
    dato = lista_nombre.eliminar('HYD195', 'codigo')
    dato.nombre = 'Nuevo nombre'
    lista_nombre.insertar(dato, 'nombre')


lista_fecha.barrido()
print()
lista_nombre.barrido()
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
dinos = ['Tyrannosaurus Rex', 'Spinosaurus', 'Giganotosaurus']
lista_nombre.dino_level(dinos, ['high', 'critical'])
print()

print('CCCCCCCCCCCCCCCC')
while(not cola_c.cola_vacia()):
    dato = cola_c.atencion()
    if(dato.codigo == 'EPC944'):
        print('&&&&&&&&&&&&&&&& dato descartado')
    else:
        print(dato)
# print('HHHHHHHHHHHHHHHH')
# while(not cola_h.cola_vacia()):
#     print(cola_h.atencion())
dinos = ['Raptors (Dromaeosauridae)', 'Carnotaurus', 'Compsognathus']
lista_nombre.dino_level(dinos, ['high', 'critical', 'low', 'medium'])

cadena = 'mosquito'

def decodificar(numero):
    if(numero >= 33 and numero <= 47):
        return chr(numero)
    else:
        if(numero % 3 == 0):
            return decodificar(numero // 2 + 9)
        else:
            return decodificar(numero -14)


cadena_decodificada = ''
for letra in cadena:
    numero = ord(letra)
    cadena_decodificada += decodificar(numero)

print(cadena_decodificada)



def criterio(item):
    return item['named_by'][-4:]

dinosaurs.sort(key=criterio)

print(dinosaurs[-1])