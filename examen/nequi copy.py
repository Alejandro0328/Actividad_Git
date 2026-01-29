def sistema_nequi():
    saldo = 0  # Variable principal para rastrear el dinero
    
    while True:
        print("\n--- BIENVENIDO A NEQUI ---")
        print("1. Cargar saldo")
        print("2. Pagar")
        print("3. Transferir dinero")
        print("4. Mostrar saldo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            monto = float(input("Ingrese el monto a cargar: "))
            if monto > 0:
                saldo += monto
                print(f"Carga exitosa. Nuevo saldo: ${saldo}")
            else:
                print("Error: El monto debe ser mayor a cero.")

        elif opcion == "2":
            monto = float(input("Ingrese el monto a pagar: "))
            if monto <= 0:
                print("Error: Monto inválido.")
            elif monto > saldo:
                print("Error: Fondos insuficientes.")
            else:
                saldo -= monto
                print(f"Pago realizado. Saldo restante: ${saldo}")

        elif opcion == "3":
            celular = input("Ingrese el número de celular del destinatario (10 dígitos): ")
            if len(celular) != 10:
                print("Error: El número debe tener exactamente 10 caracteres.")
                continue # Regresa al inicio del ciclo
            
            monto = float(input("Ingrese el monto a transferir: "))
            if monto <= 0:
                print("Error: Monto inválido.")
            elif monto > saldo:
                print("Error: Fondos insuficientes.")
            else:
                saldo -= monto
                print(f"Transferencia exitosa a {celular}. Saldo restante: ${saldo}")

        elif opcion == "4":
            print(f"Tu saldo actual es: ${saldo}")

        elif opcion == "5":
            print("Gracias por usar Nequi. ¡Hasta pronto!")
            break # Rompe el ciclo While y termina el programa

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
sistema_nequi()
