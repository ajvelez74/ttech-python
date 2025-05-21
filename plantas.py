
def calcular_Plantas ( largo, ancho, separacion ) :
    if not(largo > 0) :
        raise ValueError("El largo del terreno debe ser mayor que cero")
    if not(ancho > 0) :
        raise ValueError("El ancho del terreno debe ser mayor que cero")
    if not(separacion > 0) :
        raise ValueError("La separación entre plántulas debe ser mayor que cero")
        
    # Paso 1. Calcular la cantidad de plántulas  
    # pueden sembrar a lo largo del terreno ( plantulasLargo : número entero )
    plantulas_Largo = ( largo / separacion ) + 1

    # Paso 2. Calcular la cantidad de plántulas que 
    # se pueden sembrar a lo ancho del terreno ( plantulasAncho : número entero )
    plantulas_Ancho = ( ancho / separacion ) + 1

    # Paso 3. Calcular la cantidad total de plántulas 
    # que se pueden sembrar en el terreno ( cantidadPlantulas : número entero )

    cantidad_Plantulas = plantulas_Largo * plantulas_Ancho
    
    return cantidad_Plantulas 
# fin de la función calcularPlantas

def principal() :
    try :
        # Lectura de datos  
        cadena = input("Ingrese el largo del terreno: ")
        largo = float(cadena)

        ancho = float(input("Ingrese el ancho del terreno: "))

        separacion = float(input("Ingrese la separación entre plántulas: "))

        # LLamar la al función que resuleve el problema
        plantas = calcular_Plantas (largo, ancho, separacion)

        # Mostrar el resultado
        print("La cantidad de plántulas que se pueden sembrar es: ", plantas)
    except ValueError as e:
        print("Error: ", e)
    except Exception as e:
        print("Error inesperado: ", e)

# fin de la función principal
 
principal() 