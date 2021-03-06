

def suma(n1, n2):
    """ Esta funcion recibe dos numero y retorna la suma de ambos"""
    return n1 + n2

# print('codigo suelto fuera de funciones')

vector = [100, 0, 11, 3, 81, 7, 45, -1]


def quicksort(vec, primero, ultimo):
    pivot = ultimo
    izq = primero
    der = ultimo -1
    while(izq < der):
        while(vec[izq] < vec[pivot]) and (izq <= der):
            izq += 1
        while(vec[der] > vec[pivot]) and (der >= izq):
            der -= 1
        if(izq < der):
            vec[izq], vec[der] = vec[der], vec[izq]
    if(vec[izq] > vec[pivot]):
        vec[izq], vec[pivot] = vec[pivot], vec[izq]
    if(primero < izq):
        quicksort(vec, primero, izq-1)
    if(izq < ultimo):
        quicksort(vec, izq+1, ultimo)


# quicksort(vector, 0, len(vector)-1)

# print(vector)
def salida_laberinto(matriz, x, y, caminos=[]):
    """Salida del laberinto."""
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if(matriz[x][y] == 2):
            caminos.append([x, y])
            print("Saliste del laberinto")
            print(caminos)
            caminos.pop()
        elif(matriz[x][y] == 1):
            matriz[x][y] = 3
            caminos.append([x, y])
            # print("mover este")
            salida_laberinto(matriz, x, y+1, caminos)
            # print("mover oeste")
            salida_laberinto(matriz, x, y-1, caminos)
            # print("mover norte")
            salida_laberinto(matriz, x-1, y, caminos)
            # print("mover sur")
            salida_laberinto(matriz, x+1, y, caminos)
            caminos.pop()
            matriz[x][y] = 1


lab = [[1, 1, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 0, 1],
       [0, 1, 1, 0, 1, 0, 1],
       [1, 0, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 2]]

salida_laberinto(lab, 0, 0)




def barrido_descendente(vec):
    if(len(vec) == 1):
        print(vec[0])
    else:
        print(vec[-1])  #? print(vec[len(vec)-1])
        barrido_descendente(vec[:-1])



def barrido_descendente2(vec, pos):
    if(pos == 0):
        print(vec[pos])
    else:
        print(vec[pos])
        barrido_descendente2(vec, pos-1)




a = [1,2,3,4,5]
barrido_descendente(a)


romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50}


def romano_a_decimal(num_romano):
    if(len(num_romano) == 1):
        return romanos[num_romano]
    else:
        if(romanos[num_romano[0]] >= romanos[num_romano[1]]):
            return romanos[num_romano[0]] + romano_a_decimal(num_romano[1:])
        else:
            return - romanos[num_romano[0]] + romano_a_decimal(num_romano[1:])


print(romano_a_decimal('XXI'))


# def busqueda_sec()