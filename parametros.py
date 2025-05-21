
def calcularEdadPromedio(lista_edades) :
    suma = 0
    for edad in lista_edades :
        suma = suma + edad
    return suma / len(lista_edades)


def calcularEdadPromedio(*edades) :
    suma = 0
    for edad in edades :
        suma = suma + edad
    return suma / len(edades)

