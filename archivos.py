

with open("archivo.txt", "w") as archivo:
    archivo.write("Este es un archivo de texto plano.\n") 
    archivo.write("Se trata de un archivo cuyo contenido es texto sin formato.\n") 
# El archivo se cierra automáticamente al salir del bloque with


try:
    with open("archivos.txt", "r") as archivo:
        texto = archivo.read()
        print(texto)
    # El archivo se cierra automáticamente al salir del bloque with
except FileNotFoundError:
    print("El archivo no existe.")


with open("archivo.txt", "a") as archivo:
    archivo.write("La opción de apertura a permite agregar contenido al archivo.\n") 
# El archivo se cierra automáticamente al salir del bloque with

contador = 1
palabras = 0
with open("archivo.txt", "r") as archivo:
    while True:
        linea = archivo.readline()
        if not linea:
            break
        print(contador, linea)
        contador += 1

        palabras += len(linea.split(" "))
# El archivo se cierra automáticamente al salir del bloque with
print (f"El archivo tiene {palabras} palabras.")
