'''
Haz un script que ejecute estas acciones por pasos:
1.- Cálculo de raíz cuadrada:
Pide al usuario un número y muestra su raíz cuadrada usando la función math.sqrt().
2.- Área de un círculo:
Solicita al usuario el radio de un círculo y calcula su área utilizando math.pi y math.pow().
3.- Seno y coseno de un ángulo:
Pide al usuario un ángulo en grados y muestra su seno y coseno empleando math.sin() y
math.cos().
(Recuerda convertir los grados a radianes con math.radians().)
'''
import math

def raiz():
    numUser = float(input('Ingresa un número para la raiz cuadrada:'))
    print(f'la raiz de {numUser} es: {math.sqrt(numUser)}')

def area():
    radio = float(input('Ingresa un número para calcular el área del círculo:'))
    area = math.pi * math.pow(radio,2)
    print(f'El áreal del círculo con radio {radio} es: {area}')

def senAndCos():
    angulo = math.radians(float(input('Ingresa un ángulo en grados:')))
    sin = math.sin(angulo)
    cos = math.cos(angulo)
    print(f'El seno y coseno del ángulo {angulo}° es: {sin} , {cos}')

if __name__ == "__main__":
    senAndCos()


