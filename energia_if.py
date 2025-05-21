
def calcularValorEnergia( consumo_anterior , consumo_actual , estrato ) :

    # Calcular la cantidad de kilovatios consumidos
    consumo_kv = consumo_actual - consumo_anterior
    
    # Calcular el valor a pagar por concepto de kilovartios consumidos
    valor_consumo = consumo_kv * 200
    
    # Calcular el valor a pagar por concepto de alumbrado
    valor_alumbrado = consumo_kv * 30
    
    # Calcular el valor a pagar por concepto de cargo básico
    if (estrato == 1) or (estrato == 2) :
        cargo_basico = 2000
    elif (estrato == 3) :
        cargo_basico = 5000
    elif (estrato == 4):
        cargo_basico = 8000
    else :
        cargo_basico = 15000
    
    # Calcular el valor a pagar por concepto de subsidio o incremento
    if (estrato == 1) or (estrato == 2) :
        valor_subsidio = valor_consumo * 0.8
        valor_incremento = 0
    elif (estrato == 3) :
        valor_subsidio = valor_consumo * 0.5
        valor_incremento = 0
    elif (estrato == 4):
        valor_subsidio = 0
        valor_incremento = valor_consumo * 0.10
    else :
        valor_subsidio = 0
        valor_incremento = valor_consumo * 0.35
    
    # Calcular el valor por concepto de iva
    valor_iva = (valor_consumo + valor_alumbrado) * 0.10
    
    # Calcular el valor total a pagar
    valor_factura = valor_consumo + valor_alumbrado + cargo_basico - valor_subsidio + valor_incremento + valor_iva

    return valor_factura
# fin la funcion calcularValorEnergia

