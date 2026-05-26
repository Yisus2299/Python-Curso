#proyecto numero 10 - calculadora que decida operaciones y diga si quieres continuar o no

#1- crea una funcion para sumar

def add(n1, n2):
    return n1 + n2

#2- escribe otras 3 funciones: substract. multiply y dividir.

def substract (n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

#3- agrega estas 4 funciones en in diccionario con los valores. Keys = "+", "-", "*", "/".

operaciones = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

#4- usa el diccionario de operaciones para realizar calculos. Multiplicar 4 * 8 usando el diccionario a ver si funciona:

# print(operaciones["*"](n1 = 4, n2 = 8))

#5- pide al usuario introducir un numero, luego, crea un bucle for para recorrer todos los caracteres de las operaciones y simbolos
# Esto para que el usuario pueda ver todos los simbolos disponibles. Luego, pide al usuario poner otro numero

#6- debemos de crear otro bucle While por si quieres continuar y que este bucle acumule las cuentas en total y alli metes todo el bucle For previamente creado

#7- debemos de almacenar todo en otro bucle pero como seria confuso, lo mejor que podemos hacer es crear una funcion de Calculo que lo almacene


def calculo():
    deberias_acumular = True
    num1= float(input("Cual es el primer numero?: ")) #esta variable va afuera ya que almacena el numero y ademas, es la que inicia a su vez el bucle

    while deberias_acumular:
        for simbolo in operaciones: #esto proviene del diccionario
            print(simbolo)
        simbolo_elegir = input("Elige una operacion: ")
        num2 = float(input("Cual es el siguiente?: "))
        respuesta = operaciones[simbolo_elegir](num1, num2) # operaciones proviene del diccionario. Simbolo a elegir es de nuestro input y para que funcione, entre parentesis incluimos las variables num1,num2
        print(f"{num1} {simbolo_elegir} {num2} {respuesta}")

        #8 - una vez teniendo el resultado normalmente hecho debemos de crear una condicional para saber si quieres seguir sacando cuentas o quieres dejarlo hasta alli

        opcion = input(f"Escribe 'si' para continuar calculando con {respuesta}, o escribe 'no' para empezar un nuevo calculo.").lower()

        if opcion == "si":
            num1 = respuesta
        else:
            deberias_acumular = False
            print("\n" * 20)
            calculo()#llamamos a la funcion otra vez para ejecutar la calculadora otra vez

calculo() #llamamos a la funcion creada en lugar de crear otro while y para que sea mas practico de repetir el codigo