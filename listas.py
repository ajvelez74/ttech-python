
lista = [5,6,8,14,20,5]
listaVacia = []

print(lista[0])
print(lista[1])

def sumaListaI01(lista):
    suma = 0
    for i in range(0,len(lista)):
        suma += lista[i] # suma = suma + lista[i]
    return suma

print(sumaListaI01(lista))  # 58

def sumaListaI02(lista):
    suma = 0
    for x in lista:
        suma += x # suma = suma + x
    return suma

print(sumaListaI02(lista))  # 58


l1 = [1,2,3]
l2 = [4,5,6]

l1.append(50)
print(l1)  # 

l1.extend(l2) 
print("extends : ", l1)  # [1, 2, 3, 50, 4, 5, 6]

l1.sort()
print("sort : ", l1)  # [1, 2, 3, 4, 5, 6, 50]



# Tupla 

t = (51,25,36)
print(t[0])  # 1
print(t[1])  # 2





# Tupla para agrupar informacion
tupla = (11444444, "Juan", "Ortiz", 25, 1.75)

listasPersonas = [(11444444, "Juan", "Ortiz", 25, 1.75),
                  (11444445, "Pedro", "Gonzalez", 30, 1.80),
                  (11444446, "Maria", "Lopez", 28, 1.65),
                  (11444447, "Ana", "Martinez", 22, 1.70),
                  (11444448, "Luis", "Hernandez", 35, 1.85)]


def calcularAlturaPromedio(lista):
    if (len(lista) == 0):
        raise Exception("La lista está vacía")
    
    suma = 0
    for persona in lista:
        suma += persona[4]  # Acceder a la altura (índice 4)
    if len(lista) > 0 :
        return suma / len(lista) 


def buscarPersonaPorNUIP(lista, nuip):
    for persona in lista:
        if persona[0] == nuip:  # Comparar el DNI (índice 0)
            return persona
    #return None  # Si no se encuentra la persona
    raise Exception("No se encontró la persona con el NUIP proporcionado")


