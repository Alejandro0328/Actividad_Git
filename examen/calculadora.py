# hacer un programa que despligue un menu que permita hacer las operaciones sencillas de una calculadora (suma, resta , multi






def menu():
   print("""*** CALCULADORA SENCILLA***
1.Suma
2.Resta
3.Multiplicacion
4:Division
5.salir
------------------
Opcion (1-5)?""")
def leer_opcion():
   op = input()
   while(not op.isdigit() or int(op)< 1 or int (op)> 5):
       print("Error. digite un numero de 1 a 5.")
       input("presione culaquier tecla para continuar .......")
       print("\n\n")
       menu()
       op=input()
   return int (op)
def leer_float(msg):
       try:
           str_num = float(input(msg))
           return str_num
       except ValueError:
           print("Error. no es un numero float valido")
           input("intente nuevamente. Presione cualquier tecla para continuar")


def Suma():
   print("***1.Suma ***")
   n1 = leer_float("ingrese el primer numero:")
   n2 = leer_float("ingrese el segundo numero:")
   print(f"la suma es :{n1 + n2}")
   return n1 + n2
def resta():
   print("***2.Resta***")
   n1 = leer_float("ingrese el primer numero:")
   n2 = leer_float("ingrese el segundo numero:")
   print(f"la Resta es :{n1 - n2}")
   return n1 - n2
def multiplicacion():
   print("***3.multiplicacion***")
   n1 = leer_float("ingrese el primer numero:")
   n2 = leer_float("ingrese el segundo numero:")
   print(f"la multiplicacion es :{n1 * n2}")
   return n1 * n2
def divisiom():
   print("***4. Division***")
   n1 = leer_float("ingrese el primer numero:")
   n2 = leer_float("ingrese el segundo numero:")
   print(f"la Division es :{n1 / n2}")
   return n1 / n2
def main():
   opcion = 0
   while (opcion != 5):
       menu()
       opcion= leer_opcion()
       if opcion== 1:
           Suma()
       elif opcion ==2:
           resta()
       elif opcion== 3:
           multiplicacion()
       elif opcion== 4:
           divisiom()
       elif opcion == 5:
           print ("\n\n Gracias por usar la calculadora .ADIOS.")
       input("presione cualquier tecla para terminar ......")
       print("\n\n\n")
main()