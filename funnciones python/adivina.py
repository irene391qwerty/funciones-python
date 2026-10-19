import random 


def tirar_dados():
    
    return random.randint(2, 12) [cite: 472, 474]

def jugar():
    print("¡Bienvenido al juego de los dados!")
    
    while True:
        
        resultado_dados = tirar_dados()
        
        
        prediccion = input("¿El resultado será 'par' o 'impar'? (O escribe 'salir' para terminar): ")
        
        if prediccion.lower() == 'salir':
            print("Gracias por jugar.")
            break
            
        
        es_par = (resultado_dados % 2 == 0)
        
        
        if (prediccion.lower() == 'par' and es_par) or (prediccion.lower() == 'impar' and not es_par):
            print("¡Ganaste! El número fue: " + str(resultado_dados)) [cite: 467]
        else:
            print("Perdiste. El número fue: " + str(resultado_dados)) [cite: 467]
        print("-" * 30)


jugar()