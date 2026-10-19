
persona = {
    "nombre": "Rodrigo", 
    "apellido": "Montemayor", 
    "edad": 30 
}


print(persona)


print("El nombre es: " + persona["nombre"])


persona["edad"] = 31


persona["ciudad"] = "Monterrey"


for llave, valor in persona.items():
    print(llave + ": " + str(valor))