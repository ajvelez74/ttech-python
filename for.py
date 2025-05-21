
resultado = 0
contador = 0
valor = 0
while(contador <= 5) :
    valor = valor + 1
    if(valor % 2 == 1) :
        continue
    
    resultado = resultado + valor
    contador = contador + 1

# fin del while
print(resultado)


