def main():
    
    print("Este es el menu")
    print("1.Suma\n2.Resta\n3.Multiplica\n4.Dividir\n5.Salir")
    num = int(input("Ingrese el numero de su eleccion: "))
    while num != 5:
        if num == 1:
            funcionSumar()
        elif num == 2:
            funcionRestar()
        elif num == 3:
            funcionMultiplicar()
        elif num == 4:
            funcionDividir()
        elif num == 5:
            exit()
        else: 
            print("Opcion invalida")

def funcionSumar():
    print("Esta es la suma")
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    suma = num1 + num2
    print("La suma es: "+ str(suma))

def funcionRestar():
    print("Esta es la resta")
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    print("La suma es: "+ num1 - num2)


def funcionMultiplicar():
    print("Esta es la multiplicación")
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    print("La suma es: "+ num1 * num2)

def funcionDividir():
    print("Esta es la división")
    num1 = int(input("Ingrese el numero 1: "))
    num2 = int(input("Ingrese el numero 2: "))
    print("La suma es: "+ num1 / num2)

main()