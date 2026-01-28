def menu():print("""***LIQUIDACION DE MATRICULAS***
1. Programa Academico
2. Beca (si aplica)
3. Salir
--------------------
Opcion 1-3?""")

def menu_P():
    print("""***PROGRAMA ACADEMICO***
1. Técnico en Sistemas.
2. Técnico en Desarollo de videojuegos
3. Técnico en Animacion Digital
4. Salir
--------------------------------------
Opcion 1- 4?""")

def menu_B():
    print("""***INDICADOR DE BECA***
1. Beca por rendimiento academico (50%)
2. Beca Cultural-Deportes (40%)
3. Sin Beca
4. Salir
-------------------------------------
Opcion 1-4 ?""")

def leer_opcion_1_3():
    op = input()
    while (not op.isdigit() or int(op) < 1 or int(op) > 3):
        print("Error. Digite un número de 1 a 3")
        input("Presione cualquier tecla para continuar...")
        menu()
        op = input()
    return int(op)

def leer_opcion_1_4(tipo_menu):
    op = input()
    while (not op.isdigit() or int(op) < 1 or int(op) > 4):
        print("Error. Digite un número de 1 a 4")
        input("Presione cualquier tecla para continuar...")
        if tipo_menu == "P": menu_P()
        else: menu_B()
        op = input()
    return int(op)

def programa():
    menu_P()
    opcion = leer_opcion_1_4("P")
    costo = 0
    if opcion == 1:
        costo = 800000
    elif opcion == 2:
        costo = 1000000
    elif opcion == 3:
        costo = 1200000
    elif opcion == 4:
        print("Regresando al menú principal...")
    return costo

def calcular_beca(costo_actual):
    if costo_actual == 0:
        print("Primero debe elegir un programa académico.")
        return 0

    menu_B()
    opcion = leer_opcion_1_4("B")
    descuento = 0
    if opcion == 1:
        descuento = costo_actual * 0.5
    elif opcion == 2:
        descuento = costo_actual * 0.4
    elif opcion == 3:
        descuento = 0

    return descuento

def main():
    opcion = 0
    costo_total = 0
    descuento_aplicado = 0

    while(opcion != 3):
        menu()
        opcion = leer_opcion_1_3()
        if opcion == 1:
            costo_total = programa()
            print(f"Costo base seleccionado: ${costo_total}")
        elif opcion == 2:
            descuento_aplicado = calcular_beca(costo_total)
            if costo_total > 0:
                total_pagar = costo_total - descuento_aplicado
                print(f"Descuento: ${descuento_aplicado}")
                print(f"TOTAL A PAGAR: ${total_pagar}")
        elif opcion == 3:
            print("\nGracias por visitarnos. Hasta Pronto.")
            input("Presione cualquier tecla para terminar...")
main()