costo=0

def menu():
    print("""***LIQUIDACION DE MATRICULAS***
1.Programa Academico
2.Beca(si aplica)
3.Salir
--------------------
Opcion 1-3?""")
def menu_P():
    print("""***PROGRAMA ACADEMICO***
1. Técnico en Sistemas.
2. Técnico en Desarollo de videojuegos
3. Técnico en Animacion Digital
4.Salir
--------------------------------------
Opcion 1- 4?""")
def menu_B():
    print("""***INDICADOR DE BECA***
1. Beca por rendimiento academico
2. Beca Cultural-Deportes
3. Sin Beca
4. Salir
-------------------------------------
Opcion 1-4 ?""")
def leer_opcion_1_3():
    op= input()
    while (not op.isdigit() or int(op) < 1 or int(op)>3):
        print("Error.digite un número de 1 a 3")
        input("Presione cualquier tecla para continur......")
        print("\n\n")
        menu()
        op= input()
    return int(op)
def leer_opcion_1_4():
    op= input()
    while (not op.isdigit() or int(op) < 1 or int(op)>4):
        print("Error.digite un número de 1 a 4")
        input("Presione cualquier tecla para continur......")
        menu()
        op= input()
    return int(op)

def programa ():
        opcion=0
        while(opcion != 4):
            menu_P()
        opcion=leer_opcion_1_4()
        if opcion== 1:
            costo =(800000)
        elif opcion== 2:
            costo =(1000000)
        elif opcion==3:
            costo= int(1200000)

        elif opcion== 4:
            print("\n\n Gracias por visitarnos. Hasta Pronto.")
            input("Precione cualquier tecla para terminar....................")
            print("\n\n\n")
        return costo
def beca():
        opcion=0
        while(opcion != 4):
            menu_P()
        opcion=leer_opcion_1_4()
        if opcion== 1:
            beca = costo * 0.5
        elif opcion== 2:
            beca = costo * 0.4
        elif opcion==3:
            beca = costo * 1

        elif opcion== 4:
            print("\n\n Gracias por visitarnos. Hasta Pronto.")
            input("Precione cualquier tecla para terminar....................")
            print("\n\n\n")
        return beca
def main ():
    opcion=0
    while(opcion != 3):
        menu()
        opcion=leer_opcion_1_3()
        if opcion== 1:
            programa()
        elif opcion== 2:
            beca()
        elif opcion== 3:
            print("\n\n Gracias por visitarnos. Hasta Pronto.")
            input("Precione cualquier tecla para terminar....................")
            print("\n\n\n")
main()
    