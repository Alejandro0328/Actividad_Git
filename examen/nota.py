"""
calcular promedio
clacular nota mas alta
calcualr nota mas baja
salir


"""
def menu():
   print("""*** PROGRAMA DE NOTAS***
1.Calcular Promedio
2.Calcular nota  mas alta
3.Calcular nota mas baje
4salir
------------------
Opcion (1-4)?""")
def leer_opcion():
   op = input()
   while(not op.isdigit() or int(op)< 1 or int (op)> 4):
       print("Error. digite un numero de 1 a 4.")
       input("presione culaquier tecla para continuar .......")
       print("\n\n")
       menu()
       op=input()
   return int (op)
def leer_nota():
   while(True):
       try:
           nota=int(input("ingresa la nota:"))
           if 10 <= nota <= 50:
               return nota
           else:
               print("Error:La nota debe estar en 10 y 50")
       except ValueError:
           print("Error. solo s epermiten numeros enteros.")
def Calcular_promedio():
   nota = leer_nota()
   cont = 0
   suma =0
   while nota!= 0:
       cont+= 1
       suma+= nota
       nota =leer_nota()
   prom= suma /cont
def Calcular_alta():
   pass
def Calcular_Baja():
   pass


def main():
   opcion = 0
   while (opcion != 4):
       menu()
       opcion= leer_opcion()
       if opcion== 1:
           Calcular_promedio()
       elif opcion ==2:
           Calcular_alta()
       elif opcion== 3:
           Calcular_Baja()
       elif opcion == 4:
           print ("\n\n Gracias por usar EL PROGRAMA DE NOTAS.ADIOS.")
       input("presione cualquier tecla para terminar ......")
       print("\n\n\n")
main()