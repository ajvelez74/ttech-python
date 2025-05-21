
tupla = (11444444, "Juan", "Ortiz", 25, 1.75)
print("tupla[2] : " , tupla[2])


# Diccionario : estructura de datos organizada de la forma
#   clave : valor 
#   nuip  : tupla con informacion de la persona
#   
personas = { 11444444 : (11444444, "Juan", "Ortiz", 25, 1.75),
             11444445 : (11444445, "Pedro", "Gonzalez", 30, 1.80),
             11444446 : (11444446, "Maria", "Lopez", 28, 1.65),
             11444447 : (11444447, "Ana", "Martinez", 22, 1.70),
             11444448 : (11444448, "Luis", "Hernandez", 35, 1.85)
            }

# Consultar un elemento en el diicionario 
p = personas[11444446]
print("personas[11444446] : " , p)

apellido = p[2]
print("personas[11_444_446][2] : " , apellido)

# Agregar un elemento al diccionario
personas[11444449] = (11444449, "Carlos", "Ramirez", 29, 1.78)

print("personas.keys() : " , personas.keys())


