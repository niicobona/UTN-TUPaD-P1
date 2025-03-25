#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print ("Hola Mundo!")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#  el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#  por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#  realizar la impresión por pantalla.

nombre = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#  imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#  “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#  años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#  la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int (input("Ingrese su edad: "))
residencia = input("Ingrese lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#  su perímetro.

radio = int (input("Ingrese el radio de un círculo:"))
area = 3.14 * (radio ** 2)
perimetro = (2*3.14) * radio
print (f"El área del círculo es {area} y su perímetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#  cuántas horas equivale.

segundos = float(input("Ingrese una cantidad en segundos: "))
horas = segundos / 3600
print(f"El equivalente de {segundos} segundos en horas es de: {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#  multiplicar de dicho número.

num = int(input("Ingrese un número: "))
print (f"{num} x 1 =",num * 1)
print (f"{num} x 2 =",num * 2)
print (f"{num} x 3 =",num * 3)
print (f"{num} x 4 =",num * 4)
print (f"{num} x 5 =",num * 5)
print (f"{num} x 6 =",num * 6)
print (f"{num} x 7 =",num * 7)
print (f"{num} x 8 =",num * 8)
print (f"{num} x 9 =",num * 9)
print (f"{num} x 10 =",num * 10)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#  pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

if (num1 != 0) & (num2 != 0) :
    print(f"{num1} + {num2} = ",num1 + num2)
    print(f"{num1} - {num2} = ",num1 - num2)
    print(f"{num1} * {num2} = ",num1 * num2)
    print(f"{num1} / {num2} = ",num1 / num2)
else :
    print("Ingrese bien los numeros solicitados.")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#  de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#  modo:

altura = float(input("Por favor ingrese su altura en metros: "))
peso = float(input("Por favor ingrese su peso en kilogramos: "))
masaCorporal = peso / (altura ** 2)
print(f"El indice de masa corporal es de: {masaCorporal}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#  pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

tempCelsius = float (input("Ingrese una temperaturta en grados Celsius: "))
tempFahrenheit = (9/5) * tempCelsius + 32
print(f"La conversión de {tempCelsius}ºC a Fahrenheit es de : {tempFahrenheit}ºF") 

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#   dichos números.

num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
num3 = int(input("Ingrese tercer número: "))

promedio = (num1 + num2 + num3) / 3
print (f"El promedio de los 3 números es de: {promedio}")


