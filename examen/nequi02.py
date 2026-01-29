def menu():
    print("""***BIENVENIDO A NEQUI***
--Que desea hacer--
1.Cargar saldo
2.Pagar
3.Transferir dinero
4.Mostrar saldo
5.Salir
-------------------
Opcion 1 - 5 ?""")
def pagar():
    pass
def cargarsaldo():
    pass
def tranferir():
    pass
def mostrar():
    pass
def main ():
    opcion = 0
    while opcion != 5:
        menu()
    if opcion == 1:
        cargarsaldo()
    elif opcion == 2:
        pagar()
    elif opcion == 3:
        tranferir()
    elif opcion == 4:
        mostrar()
    elif opcion == 5:
        print("Gracias por usar NEQUI.Adios")
        input("Presione cual quier letra para comtinuar")
main()
