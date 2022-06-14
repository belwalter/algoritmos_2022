from jurassic_park import dinosaurs

def busqueda(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']


file = open('alerts.txt')

lineas = file.readlines()
lineas.pop(0)

for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda(dato[2]))
    print(dato)
