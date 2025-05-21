
CARGO_BASICO = [0, 2000, 2000, 5000, 8000, 15000, 15000]
PORCETAJE_SUBSIDIO    = [0, 0.8, 0.8, 0.5,    0,    0,    0]
PROCENTAJE_INCREMENTO = [0, 0,     0,   0, 0.10, 0.35, 0.35]

def calcularValorEnergia( consumo_anterior , consumo_actual , estrato ) :

    # Calcular la cantidad de kilovatios consumidos
    consumo_kv = consumo_actual - consumo_anterior
    
    # Calcular el valor a pagar por concepto de kilovartios consumidos
    valor_consumo = consumo_kv * 200
    
    # Calcular el valor a pagar por concepto de alumbrado
    valor_alumbrado = consumo_kv * 30
    
    # Calcular el valor a pagar por concepto de cargo básico    
    valor_cargo_basico = CARGO_BASICO[estrato]
    
    # Calcular el valor a pagar por concepto de subsidio o incremento
    valor_subsidio = valor_consumo * PORCETAJE_SUBSIDIO[estrato]
    valor_incremento = valor_consumo * PROCENTAJE_INCREMENTO[estrato]
 
    # Calcular el valor por concepto de iva
    valor_iva = (valor_consumo + valor_alumbrado) * 0.10
    
    # Calcular el valor total a pagar
    valor_factura = valor_consumo + valor_alumbrado + valor_cargo_basico - valor_subsidio + valor_incremento + valor_iva

    return valor_factura
# fin la funcion calcularValorEnergia

