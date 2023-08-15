print("Ingrese el nombre del asociado:")
asociado = input()
print("Ingrese la edad del asociado:")
edad = int(input())

categoria = ""

if edad >= 13 and edad < 15:
    categoria = "infantiles"
elif edad >= 15 and edad < 17:
    categoria = "cadetes"
elif edad >= 17 and edad < 19:
    categoria = "juveniles"
elif edad >= 19:
    categoria = "mayores"

print (f"El asociado {asociado} pertenece a la categoria {categoria}")