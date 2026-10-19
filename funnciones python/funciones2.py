nombre_usuario = "Rodrigo"
# Uso de la función integrada len() para obtener la longitud de un texto
longitud = len(nombre_usuario) [cite: 308]
print("Longitud del nombre:")
print(longitud)

# Función con un parámetro con valor por defecto
def calcular_total(precio, impuesto=0.16):
    return precio + (precio * impuesto)

# Se puede llamar con un solo argumento (usa el impuesto por defecto)
print(calcular_total(100))
# O sobreescribiendo el parámetro opcional
print(calcular_total(100, 0.08))