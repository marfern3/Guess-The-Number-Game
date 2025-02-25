import random

while True:
    numero_secreto = random.randint(1, 100)
    numero = 1
    max_intento = 10

    print('¡Bienvenido al juego de adivinar el número!')
    print('Adivina el número entre 1 y 100 en un máximo de 10 intentos.')

    while numero <= max_intento:
        try:
            intento = int(input(f'Intento {numero}: '))
            if intento < 0 or intento > 100:
                print("⚠️ El número debe estar entre 0 y 100. Intenta de nuevo")
        except:
            print("⚠️ Introduce un número válido por favor")
            continue

        if intento == numero_secreto:
            print(f'🎉!Felicidades ese era el número, te costo {numero} intentos!🎉')
            break
        elif intento < numero_secreto:
            print('El número secreto es mayor')
        elif intento > numero_secreto:
            print('El número secreto es menor')

        numero += 1

    if numero > max_intento:
        print(f'Se acabaron los intentos. El número secreto era {numero_secreto}')

    jugar_de_nuevo = input('¿Quieres jugar otra vez? (s/n): ').lower()
    if jugar_de_nuevo != 's':
        print('¡Gracias por jugar!')
        break
