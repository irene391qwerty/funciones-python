nombres = ["Rodrigo", "Juan", "Pedro"] [cite: 760]

# Imprimir la lista completa
print(nombres) [cite: 763]

# Acceso individual mediante índices (comenzando en 0)
print(nombres[0])  # Imprime: Rodrigo [cite: 766]

# Modificar un elemento de la lista
nombres[1] = "Carlos"

# Agregar un nuevo elemento al final
nombres.append("Ana")

# Iterar una lista con un ciclo for
for nombre in nombres:
    print("Nombre: " + nombre)