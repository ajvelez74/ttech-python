

CONSTANTES = {1:(2000,0.8,0), 
              2:(2000,0.8,0),
              3:(5000,0.5,0),
              4:(8000,0.0,0.10),
              5:(15000,0.0,0.35),
              6:(15000,0.0,0.35)}

def calcularValorEnergia( consumo_anterior , consumo_actual , estrato ) :

    # Calcular la cantidad de kilovatios consumidos
    consumo_kv = consumo_actual - consumo_anterior
    
    # Calcular el valor a pagar por concepto de kilovartios consumidos
    valor_consumo = consumo_kv * 200
    
    # Calcular el valor a pagar por concepto de alumbrado
    valor_alumbrado = consumo_kv * 30
    
    # Calcular el valor a pagar por concepto de cargo básico    
    valor_cargo_basico = CONSTANTES[estrato][0]
    
    # Calcular el valor a pagar por concepto de subsidio o incremento
    valor_subsidio = valor_consumo * CONSTANTES[estrato][1]   # Subsidio
    valor_incremento = valor_consumo * CONSTANTES[estrato][2] # Incremento
 
    # Calcular el valor por concepto de iva
    valor_iva = (valor_consumo + valor_alumbrado) * 0.10
    
    # Calcular el valor total a pagar
    valor_factura = valor_consumo + valor_alumbrado + valor_cargo_basico - valor_subsidio + valor_incremento + valor_iva

    return valor_factura
# fin la funcion calcularValorEnergia

