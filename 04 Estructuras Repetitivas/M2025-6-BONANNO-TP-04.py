# Ejericio 1

for n in range (101):
    print(n)

# Ejercicio 2

num = input("Ingrese un numero entero: ")
contador = 0
for i in range (len(num)):
    contador += 1
print (f"El numero ingresado tiene {contador} digitos ")

# Ejercicio 3

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
sumatoria = 0
for i in range (num1, num2 + 1):
    sumatoria += i
print(f"La suma de todos los números enteros comprendidos entre los valores dados es de: {sumatoria}")

# Ejercicio 4

num = int(input("Ingrese un numero entero: "))
sumatoria = num
while num != 0 :
    num = int(input("Ingrese un numero entero: "))
    sumatoria += num
print (f"La suma de todos los números enteros ingresados es de: {sumatoria}")

# Ejercicio 5

import random
numAleatorio = random.randint(0,9)
print(f"numero aleatorio {numAleatorio}")
num = int(input("Adivine el numero aleatorio entre 0 y 9: "))
intentos = 1
while numAleatorio != num :
    num = int(input("Adivine el numero aleatorio entre 0 y 9: "))
    intentos += 1
print(f"Usted ha acertado el número en {intentos} intentos, FELICITACIONES!!!")

# Ejercicio 6

print ("Los números pares entre (0,100),de manera decreciente son: ")
for i in range (100,-1,-1):
    if i % 2 == 0:
        print(i)

# Ejercicio 7

num = int(input("Ingrese un número entero positivo: "))
sumatoria = 0
if num > 0 :
    for i in range (0,num + 1) :
        sumatoria += i
    print(f"La sumatoria de la secuencia de números es de: {sumatoria}")
else:
    print("El numero ingresado no es correcto, vulve a intentarlo")

#Ejercicio 8

contador = 0
num_pares = 0
num_impares = 0
num_positivos = 0
num_negativos = 0

while contador != 100:
    num = int(input("Ingrese un número entero: "))
    if num > 0 :
        num_positivos += 1
        if num % 2 == 0:
            num_pares +=1
        else:
            num_impares += 1
    elif num < 0 :
        num_negativos += 1
        if num % 2 == 0:
            num_pares +=1
        else:
            num_impares += 1        
    contador += 1

print(f"Números pares: {num_pares}\nNúmeros impares: {num_impares}\nNúmeros negativos: {num_negativos}\nNúmeros positivos: {num_positivos}")

# Ejercicio 9

contador = 0
sumatoria = 0

while contador != 100:
    num = int(input("Ingrese un número entero: "))
    sumatoria += num
    contador += 1

num_media = float(sumatoria/contador)
print(f"La media de los números ingresados es de: {num_media}")

# Ejercicio 10

num = int(input("Ingrese un numero: "))
num = str(num)
num_invertido = ""

for i in range (len(num)-1, -1, -1):
    num_invertido += num[i]

print(f"El nçumero invertido es: {num_invertido}")