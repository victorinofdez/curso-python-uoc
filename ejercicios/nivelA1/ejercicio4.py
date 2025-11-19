'''
Ejercicio 4 - Libreria datetime
Haz un script que ejecute estas acciones por pasos:
Fecha y hora actual:
Muestra la fecha y hora actuales con datetime.datetime.now().
Cálculo de edad:
Pide al usuario su año de nacimiento y calcula su edad actual usando datetime.date.today().year.
Días restantes del año:
Calcula cuántos días faltan para que termine el año con datetime.date.today() y
datetime.date.replace().

'''
import datetime


def yearOldCalc(input):
    year = int(datetime.date.today().year)
    return year - int(input)

def daysCalc():
    today = datetime.date.today()
    lastDay = today.replace(month=12, day=31)
    print(f'Los dias que faltan para que termine el año son: {(lastDay - today).days}')

if __name__ == "__main__":
    
    print(f'Fecha actual: {datetime.datetime.now()}')
    input = input('Dime el año de tu nacimiento: ')
    print(f'Tu edad es de: {yearOldCalc(input)}')
    daysCalc()
