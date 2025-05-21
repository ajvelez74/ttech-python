
def calcularValorPagar ( valorProducto ) :
    
    if not(valorProducto > 0):
        raise ValueError("El valor del producto debe ser mayor a cero")

    if (valorProducto < 20000) :
    	valorDescuento = valorProducto * 0.20
    else:
        valorDescuento = valorProducto * 0.10
    
    valorPagar = valorProducto - valorDescuento
    
    return valorPagar
# fin de la función calcularValorPagar

def principal() :

    while True:
        try :
            # Lectura de datos  int / float
            valorProducto = int ( input("Digite el valor del producto ... ") )
            # Llamar a la función que resuelve el problema
            valorPagar = calcularValorPagar(valorProducto)
            # Mostrar el resultado
            print(f"El valor a pagar es de {valorPagar} pesos")

            print("\n")
            opcion = input("Desea registrar otra compra? (s/n) ")
            if(opcion == 'n' or opcion == 'N') :
                break
        except ValueError as e:
            print("Error: ", e)
        except Exception as e:
            print("Error inesperado: ", e)
        
        print("\n")
# fin de la función principal 

principal()