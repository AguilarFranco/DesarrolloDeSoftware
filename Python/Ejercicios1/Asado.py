print("Franco, ingresá la cantidad de invitados.")
invitados = int(input())
print("Ahora ingresá el precio de la carne por kg.")
precio = float(input())
totalDeCarne = invitados * 0.7
precioTotal = invitados * precio

print (f"Para el asado se necesitan {totalDeCarne} kg de carne y un total de ${precioTotal} para pagar.")