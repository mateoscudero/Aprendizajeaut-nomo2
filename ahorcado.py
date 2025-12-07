import random

def pedir_letra(letras_usadas):
    letra = input("Ingresa una letra: ").lower()

    # Validar que sea solo un carácter
    if len(letra) != 1:
        print("Debe ser solo una letra.")
        return None

    # Validar que no se haya usado antes
    if letra in letras_usadas:
        print("Ya usaste esa letra.")
        return None

    return letra

def procesar_acierto(letra, palabra, progreso):
    for i in range(len(palabra)):
        if palabra[i] == letra:
            progreso[i] = letra

    print("Progreso:", " ".join(progreso))

    if "_" not in progreso:
        return True
    return False

def jugar():
    print("====== JUEGO DEL AHORCADO ======")

    palabras = ["casa", "perro", "gato", "sol"]
    palabra = random.choice(palabras)
    progreso = ["_"] * len(palabra)
    intentos = 6
    letras_usadas = []

    while intentos > 0:
        print("\nPalabra:", " ".join(progreso))
        print("Intentos restantes:", intentos)
        print("Letras usadas:", letras_usadas)

        letra = pedir_letra(letras_usadas)
        if letra is None:
            continue

        letras_usadas.append(letra)

        if letra in palabra:
            victoria = procesar_acierto(letra, palabra, progreso)
            if victoria:
                print("\n¡FELICIDADES, GANASTE!")
                print("La palabra era:", palabra)
                return
        else:
            print("Fallaste, esa letra no está.")
            intentos -= 1

    print("\nPerdiste. No te quedaron intentos.")
    print("La palabra correcta era:", palabra)

if __name__ == "__main__":
    jugar()
