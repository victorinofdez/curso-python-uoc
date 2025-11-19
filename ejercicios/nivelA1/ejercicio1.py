'''
Prueba la función input() en el intérprete o en un script, ¿que hace? No lo sabes?
Busca en la web.
- Ahora con esta función haz un script que te pida tu nombre y te salude.
- A continuación, haz un script que te pida tu nombre y te salude, un color y un
objeto o lugar y genera una frase con las 3 variables.
'''

if __name__ == "__main__":
    nombre = input('Escribe tu nombre: ')
    color = input('Escribe un color: ')
    lugar = input('Escribe un lugar: ')
    print(f'Hola {nombre}!, tu color es {color} y el lugar es {lugar}.')