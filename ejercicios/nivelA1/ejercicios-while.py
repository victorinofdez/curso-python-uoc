# ============================
#   EJERCICIOS CON WHILE
# ============================

def contar_hasta_10():
    """
    Debe usar un bucle while para mostrar los números del 1 al 10 separados por comas.
    Debe retornar un string, por ejemplo: "1,2,3,4,5,6,7,8,9,10"
    """
    # TODO: Implementar

    #numeros = list(range(1, 11))
    #return ", ".join(str(n) for n in numeros)

    count = 1
    coma = ', '
    cadena = ''
    while count <= 10:
        if count < 10:
            cadena += str(count) + coma
        else:
            cadena += str(count)
        count += 1
    print('esto es cadena',cadena)
    return cadena




def suma_hasta_cero():
    """
    Pedir números al usuario hasta que introduzca 0.
    Sumar todos los números (excepto el 0 final) y devolver el resultado.
    Usa un while.

    IMPORTANTE: para testear este ejercicio no se usará input(),
    sino que el alumno debe simular la lógica sin input real.
    En este archivo solo retorna un valor de ejemplo.
    """
    # TODO: Implementar la lógica sin usar input()
    userNumber = int(input('Introduce un número: '))
    suma = userNumber
    if userNumber != 0:
        while userNumber > 0:
            userNumber = int(input('Introduce otro número, si quieres salir introduce 0: '))
            suma += userNumber
        print(suma)
    return suma



def adivinar_numero():
    """
    Simula un juego donde el número secreto es 7.
    Usa un while que repita intentos hasta acertar.
    Para pruebas, simula una secuencia de intentos: 3, 5, 7.
    Retorna la cantidad de intentos usados.
    """
    # TODO: Implementar
    secrerNumber = 7
    userNumber = int(input('Introduce un número:'))
    count = 1
    acierto = False
    if(userNumber == secrerNumber):
        print(f'Enhorabuena!! el número secreto era {userNumber}')
    else:
        while userNumber != secrerNumber:
            userNumber = int(input('Ese no es el número secreto, prueba otro:'))
            count += 1
            acierto = True
        if(acierto): print(f'Enhorabuena!! el número secreto era {userNumber}')
    return count


if __name__ == "__main__":
    print("Ejecutando tests...")

    # ------- Test contar_hasta_10 -------
    assert contar_hasta_10() == "1,2,3,4,5,6,7,8,9,10", \
        f"contar_hasta_10() debería devolver '1,2,3,4,5,6,7,8,9,10', pero devolvió {contar_hasta_10()}"

    # ------- Test suma_hasta_cero -------
    # Para pruebas: 5 + 3 + 2 = 10
    # (El alumno debe simularlo en su código)
    print("Cuando te lo pida introduce los numeros 5,3 y 2")
    assert suma_hasta_cero() == 10, \
        f"suma_hasta_cero() debería devolver 10, pero devolvió {suma_hasta_cero()}"

    # ------- Test adivinar_numero -------
    # Secuencia simulada: 3, 5, 7 → 3 intentos
    assert adivinar_numero() == 3, \
        f"adivinar_numero() debería devolver 3, pero devolvió {adivinar_numero()}"
