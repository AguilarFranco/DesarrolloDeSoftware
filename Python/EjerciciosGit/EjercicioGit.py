def main():
    valor1 = None
    valor2 = None
    
    while True:
        print("1. Ingresar valor 1")
        print("2. Ingresar valor 2")
        print("3. Mostrar suma")
        print("4. Mostrar resta")
        print("5. Mostrar multiplicación")
        print("6. Mostrar división")
        print("7. Salir")
        
        opcion = int(input("\nElija una opción: "))
        
        if opcion == 1:
            valor1 = float(input("Ingrese el primer valor: "))
        elif opcion == 2:
            valor2 = float(input("Ingrese el segundo valor: "))
        elif opcion == 3:
            if valor1 is None or valor2 is None:
                print("Debe ingresar ambos valores antes de realizar la operación.")
            else:
                print("Suma:", valor1 + valor2)
        elif opcion == 4:
            if valor1 is None or valor2 is None:
                print("Debe ingresar ambos valores antes de realizar la operación.")
            else:
                print("Resta:", valor1 - valor2)
        elif opcion == 5:
            if valor1 is None or valor2 is None:
                print("Debe ingresar ambos valores antes de realizar la operación.")
            else:
                print("Multiplicación:", valor1 * valor2)
        elif opcion == 6:
            if valor1 is None or valor2 is None:
                print("Debe ingresar ambos valores antes de realizar la operación.")
            else:
                if valor2 == 0:
                    print("No es posible dividir por cero.")
                else:
                    print("División:", valor1 / valor2)
        elif opcion == 7:
            print("Saliendo del programa.")
            break
        else:
            print("Opción incorrecta. Elija una opción válida.")

if __name__ == "__main__":
    main()