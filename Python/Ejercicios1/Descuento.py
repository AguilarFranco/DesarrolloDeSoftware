print("Ingrese el monto de la compra:")
monto = float(input())

if monto > 3500:
    importe = monto - (monto*0.1)
else : importe = monto

print (f"El importe final es de: {importe}")