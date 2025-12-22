import random

# Diccionario de categorías y palabras (tuplas)
palabras_dict = {
    "Animales": ("perro", "gato", "elefante", "jirafa"),
    "Objetos": ("casa", "silla", "mesa", "laptop"),
    "Frutas": ("manzana", "banana", "pera", "uva")
}

def elegir_palabra():
    categorias = list(palabras_dict.keys())
    categoria = random.choice(categorias)
    palabras = palabras_dict.get(categoria, ())
    if not palabras:
        return "Sin categoría", ""
    palabra = random.choice(palabras)
    return categoria, palabra

def pedir_letra(letras_usadas):
    while True:
        letra = input("Ingresa una letra: ").lower()
        if len(letra) != 1:
            print("Debe ser solo una letra.")
        elif letra in letras_usadas:
            print("Ya usaste esa letra.")
        elif not letra.isalpha():
            print("Debes ingresar solo letras.")
        else:
            return letra

def procesar_acierto(letra, palabra, progreso):
    acierto = False
    for i, l in enumerate(palabra):
        if l == letra:
            progreso[i] = letra
            acierto = True
    return acierto

def jugar():
    categoria, palabra = elegir_palabra()
    progreso = ["_"] * len(palabra)
    intentos = 6
    letras_usadas = []

    print(f"\nCategoría: {categoria}")

    while intentos > 0:
        print("\nPalabra:", " ".join(progreso))
        print("Intentos restantes:", intentos)
        print("Letras usadas:", letras_usadas)

        letra = pedir_letra(letras_usadas)
        letras_usadas.append(letra)

        if procesar_acierto(letra, palabra, progreso):
            print(f"¡Bien hecho! La letra '{letra}' está en la palabra.")
            if "_" not in progreso:
                print(f"\n¡FELICIDADES, GANASTE! La palabra era '{palabra}'.")
                break
        else:
            print(f"Fallaste, la letra '{letra}' no está en la palabra.")
            intentos -= 1
            if intentos == 0:
                print(f"\nPerdiste. La palabra correcta era '{palabra}'.")
                break

# Bucle principal para volver a jugar
if __name__ == "__main__":
    while True:
        print("====== JUEGO DEL AHORCADO ======")
        jugar()
        respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if respuesta != "s":
            print("Gracias por jugar. ¡Hasta luego!")
            break