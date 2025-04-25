def main():
    x = int(input("Ingresar el valor de x: "))
    print("x al cuadrado es", square(x))
    PiedraPapelTijera()
    CasasHP()

def square(n):
    return n*n


## Ejemplo de PatternMatching
import random
def PiedraPapelTijera():
    Jugada1 = random.choice(["Piedra","Piedra","Piedra","Papel","Tijera"])
    Jugada2 = random.choice(["Piedra","Piedra","Piedra","Papel","Tijera"])

    print("Jugador 1:", Jugada1,"- Jugador 2:", Jugada2)

    if(Jugada1 == Jugada2): print("Empate")

    else:
        match (Jugada1, Jugada2): ## El patternMatching occure comparando las Jugadas con los strings en cada Case
            case ("Piedra", "Tijera"):
                print("Gana el jugador 1")
            case ("Papel", "Piedra"):
                print("Gana el jugador 1")
            case ("Tijera", "Papel"):
                print("Gana el jugador 1")
            case _:
                print("Gana el jugador 2")
        
## Ejemplo de Diccionarios

def CasasHP():
    students = {
        "Harry": "Gryffindor",
        "Hermione": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
        "Luna": "Ravenclaw"
    }

    ## Los diccionarios se crean con {} y matchean una KEY con un VALUE como en JSON

    print("Los personajes de Harry Potter pertenecen a las siguientes Casas:")

    for student in students:
        print(student, students[student], sep=", ")

main()