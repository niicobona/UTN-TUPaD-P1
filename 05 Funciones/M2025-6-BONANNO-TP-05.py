# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo ()

# Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}, Bienvenido!")
saludar_usuario(input("Ingrese su nombre: "))

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
informacion_personal(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su edad: "), input("Ingrese su residencia: "))

# Ejercicio 4
import math
def calcular_area_circulo(radio):
     return math.pi * (radio ** 2)
def calcular_perimetro_circulo(radio):
      return 2 * math.pi * radio
radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area del circulo es: {area} y el perimetro es: {perimetro}")

# Ejercicio 5
def segundos_a_horas(segundos):
    horas= segundos / 3600
    print(f"{segundos} segundos equivalen a {horas} horas.")
segundos_a_horas(float(input("Ingrese la cantidad de segundos: ")))


# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range (1, 10 + 1):
        print(f"{numero} x {i} = {numero * i }")
tabla_multiplicar (int(input("Ingrese un numero: ")))

# Ejercicio 7
def operaciones_basicas(a, b):
    operaciones= (a + b, a - b, a * b, a / b)    
    print(f"suma = {operaciones[0]}\nresta = {operaciones[1]}\nmultiplicación = {operaciones[2]}\ndivisión = {operaciones[3]}")
operaciones_basicas (int(input("Ingrese el primer numero: ")),int(input("Ingrese el segundo numero: ")))

# Ejercicio 8
import math
def calcular_imc(peso, altura):
    masa_corporal= round(peso / altura,2)
    print(f"El índice de masa corporal del usuario es: {masa_corporal}")
calcular_imc(float(input("Ingrese su peso en kilogramos: ")), float(input("Ingrese su altura en metros: ")))

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    temperatura_fahrenheit = (celsius * 1.8) + 32
    print(f"{temperatura_celsius}ºC (grados celsius) equivalen a {temperatura_fahrenheit}ºF (grados fahrenheit)")
temperatura_celsius = float(input("Ingrese la temperatura en grados celsius: "))
celsius_a_fahrenheit(temperatura_celsius)

# Ejercicio 10
def calcular_promedio(a, b, c):
    promedio =  (a + b + c) / 3
    print(f"El promedio de los tres numeros ingresados es de: {promedio}")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
calcular_promedio(a,b,c)

