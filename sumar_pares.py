
# Hacer la suma de los primeros n número pares
# por ejemplo, n = 5, entonces 
# sumar(5) = 2 + 4 + 6 + 8 + 10


def sumarPares(n) :
    contador = 1
    resultado = 0
    valor = 2
    
    while ( contador <= n ) :
        resultado = resultado + valor
        contador = contador + 1
        valor = valor + 2
    # fin del while

    return resultado
# fin de la función sumarPares

print( sumarPares(5) )

