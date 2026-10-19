def saludar_terricola():
    print("Hola, terrícola.")

# Llamar a la función
saludar_terricola()


# Función que recibe un parámetro
def saludar(nombre):
    print("Hola, " + nombre + ".")

# Llamar pasándole un argumento
saludar("Rodrigo")


# Función con retorno para conversión de temperatura
def celsius_a_fahrenheit(celsius):
    resultado = (celsius * 9 / 5) + 32
    return resultado

# Guardar el valor retornado e imprimirlo
grados_f = celsius_a_fahrenheit(25)
print(grados_f)