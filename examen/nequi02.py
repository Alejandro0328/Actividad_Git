# --- DEFINICIÓN DE FUNCIONES (Las herramientas) ---

def cargar_saldo(saldo_actual):
    monto = float(input("Ingrese el monto a cargar: "))
    if monto > 0:
        nuevo_saldo = saldo_actual + monto
        print(f"Carga exitosa. Nuevo saldo: ${nuevo_saldo}")
        return nuevo_saldo  # Devolvemos el valor actualizado
    else:
        print("Error: El monto debe ser mayor a cero.")
        return saldo_actual # Devolvemos el mismo saldo sin cambios

def realizar_pago(saldo_actual):
    monto = float(input("Ingrese el monto a pagar: "))
    if monto <= 0:
        print("Error: Monto inválido.")
    elif monto > saldo_actual:
        print("Error: Fondos insuficientes.")
    else:
        saldo_actual -= monto
        print(f"Pago realizado. Saldo restante: ${saldo_actual}")
    return saldo_actual

def transferir_dinero(saldo_actual):
    celular = input("Ingrese el número de celular (10 dígitos): ")
    if len(celular) != 10:
        print("Error: El número debe tener 10 dígitos.")
        return saldo_actual
    
    monto = float(input("Ingrese el monto a transferir: "))
    if monto <= 0:
        print("Error: Monto inválido.")
    elif monto > saldo_actual:
        print("Error: Fondos insuficientes.")
    else:
        saldo_actual -= monto
        print(f"Transferencia exitosa a {celular}. Saldo restante: ${saldo_actual}")
    return saldo_actual

# --- PROGRAMA PRINCIPAL (El director de orquesta) ---

def sistema_nequi():
    saldo = 0
    
    while True:
        print("\n--- MENÚ NEQUI (MODULAR) ---")
        print("1. Cargar saldo\n2. Pagar\n3. Transferir\n4. Ver saldo\n5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            saldo = cargar_saldo(saldo) # La función hace el trabajo y nos da el resultado
        elif opcion == "2":
            saldo = realizar_pago(saldo)
        elif opcion == "3":
            saldo = transferir_dinero(saldo)
        elif opcion == "4":
            print(f"Saldo actual: ${saldo}")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Arrancar el programa
sistema_nequi()
