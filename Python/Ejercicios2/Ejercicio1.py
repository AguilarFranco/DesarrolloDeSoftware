import random
listaAleatorios = [random.randint(1,20) for _ in range(10)]
print(listaAleatorios)

def cantidadMayores(lista, entero):
    cantidad = 0
    for elem in lista:
        if elem > entero:
            cantidad += 1
    return cantidad

print("Ingrese un número: ")
numero = int(input())
print(f"La cantidad de valores mayores a {numero} es: {cantidadMayores(listaAleatorios, numero)}")


def promedio(lista):
    suma = 0
    for elem in lista:
        suma += elem
    return suma / len(lista)

print(f"El promedio de la lista es: {promedio(listaAleatorios)}")


def valorMayor(lista):
    mayor = 0
    for elem in lista:
        if elem > mayor:
            mayor = elem
    return mayor

def valorMenor(lista):
    menor = 30
    for elem in lista:
        if elem < menor:
            menor = elem
    return menor

print(f"El mayor valor de la lista es: {valorMayor(listaAleatorios)} y el menor valor es: {valorMenor(listaAleatorios)}")

