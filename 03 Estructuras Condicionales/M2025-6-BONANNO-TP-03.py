# Ejercicio 1

edad = int(input("Ingrese su edad:"))
if edad > 18 :
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ejercicio 2

nota = int(input("Ingrese su calificación:"))

if nota >= 6 :
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3

num = int(input("Ingrese un numero par:"))
if (num % 2 == 0) :
    print("Ha ingresado un número par ")
else: 
    print("Por favor ingrese un número par")

# Ejercicio 4

edad = int(input("Ingrese su edad:"))
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# Ejercicio 5

password = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
passwordLen = len(password)
if passwordLen >= 8 and passwordLen <= 14 :
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana > moda :
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda :
    print("Sesgo negativo (a la izquierda)")
else:
    print("No hay sesgo")

# Ejercicio 7

texto = input("Ingrese una frase o palabra: ")
ultimoCaracter = texto[-1]
if ultimoCaracter == "a" or ultimoCaracter == "e" or ultimoCaracter == "i" or ultimoCaracter == "o" or ultimoCaracter == "u" or ultimoCaracter == "A" or ultimoCaracter == "E" or ultimoCaracter == "I" or ultimoCaracter == "O" or ultimoCaracter == "U" :
    texto += "!"
print(texto)

#Aca esta el mismo codigo mas optimo
texto = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if texto and texto[-1] in vocales :
    texto += "!"    
print (texto)

# Ejercicio 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opcion 1, 2 o 3: "))
if opcion == 1 :
    print(nombre.upper())
elif opcion == 2 :
    print(nombre.lower())
elif opcion == 3 :
    print(nombre.title())

# Ejercicio 9

magnitudTerremoto = float(input("Ingrese la magnitud de un terremoto segun la escala de Richter: "))
if magnitudTerremoto < 3 :
    print("Muy leve")
elif magnitudTerremoto >= 3 and magnitudTerremoto < 4 :
    print("Leve")
elif magnitudTerremoto >= 4 and magnitudTerremoto < 5 :
    print("Moderado")
elif magnitudTerremoto >= 5 and magnitudTerremoto < 6 :
    print("Fuerte")
elif magnitudTerremoto >= 6 and magnitudTerremoto < 7 :
    print("Muy fuerte")
elif magnitudTerremoto >= 7 :
    print("Extremo")

# Ejercicio 10

hemisferio = input("Introduce el hemisferio (N/S): ").upper()
mes = int(input("Introduce el mes en numero (1-12): "))
dia = int(input("Introduce el dia: "))
if hemisferio == "N" :
    if (21<= dia <= 31 and mes == 12) or (1 <= mes <=2) or (1 <= dia <= 20 and mes == 3):
        print("Usted se encuentra en Invierno")
    elif (21 <= dia <= 31 and mes == 3) or (4 <= mes <= 5) or (1 <= dia <= 20 and mes == 6):
        print("Usted se encuentra en Primavera")
    elif (21 <= dia <= 30 and mes == 6) or (7 <= mes <= 8) or (1 <= dia <= 20 and mes == 9):
        print("Usted se encuentra en Verano")
    elif (21 <= dia <= 30 and mes == 9) or (10 <= mes <= 11) or (1<= dia <=20 and mes == 12):
        print("Usted se encuentra en Otoño")
elif hemisferio == "S":
    if (21<= dia <= 31 and mes == 12) or (1 <= mes <=2) or (1 <= dia <= 20 and mes == 3):
        print("Usted se encuentra en Verano")
    elif (21 <= dia <= 31 and mes == 3) or (4 <= mes <= 5) or (1 <= dia <= 20 and mes == 6):
        print("Usted se encuentra en Otoño")
    elif (21 <= dia <= 30 and mes == 6) or (7 <= mes <= 8) or (1 <= dia <= 20 and mes == 9):
        print("Usted se encuentra en Invierno")
    elif (21 <= dia <= 30 and mes == 9) or (10 <= mes <= 11) or (1<= dia <=20 and mes == 12):
        print("Usted se encuentra en Primavera")



