'''
Ejercicio 6 - Libreria random

Escoge uno de los siguientes ejercicios y haz un script con el programa.

Juego de adivinar el número:
Genera un número aleatorio entre 1 y 10 con random.randint() y pide al usuario que lo adivine.
Muestra un mensaje indicando si ha acertado o no.

Promedio de números aleatorios:
Genera tres números aleatorios entre 1 y 100 usando random.randint(), muéstralos por pantalla y
calcula su promedio.

Simulación de un dado:
Crea un programa que muestre un número aleatorio del 1 al 6 cada vez que se ejecuta, usando
random.randint().

'''

import random


def askNumber(randomNumber):
    userNumber = int(input('introduce un número entre el 1 al 10:'))

    if userNumber >= 0 and userNumber <= 10:
        while userNumber != randomNumber:
            userNumber = int(input('No es el número correcto, ingresa otro:'))
        print(f'!Enhorabuena has acertado!, El número era {randomNumber} y tu numero era {userNumber}')  
    else:
        print(f'Ingresa un número Válido entre 0 y 10')              

def generateRandomNumbers(number):
    numbers=[]
    for _ in range(number):
        numbers.append(random.randint(0,100))
    return numbers

def media(numeros):
    suma = 0
    for num in numeros:
        suma += num
    total = suma/len(numeros)
    return total

def dado():
    return random.randint(1,6)

if __name__ == '__main__':

    #randomNumber = random.randint(0,10) 
    #askNumber(randomNumber)
    

    #numeros = generateRandomNumbers(3)
    #total = media(numeros)
    #print(numeros, total)

    res = dado()
    print(res)