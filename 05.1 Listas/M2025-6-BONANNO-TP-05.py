# Ejercicio 1
lista = []
for i in range(1,101):
    if i % 4 == 0:
        lista.append(i)

print(lista)

# Ejercicio 2
lista_deporte = ["Futbol", "Handball", "Basquet", "Tenis", "Voley"]
print("El penultimo elemento es:",lista_deporte[-2])

# Ejercicio 3 
lista_vacia = []

lista_vacia.append("Viajar")
lista_vacia.append("Comer")
lista_vacia.append("Leer")
print(lista_vacia)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[-3] = "loro"
animales[-1] = "oso"

print(animales)

# Ejercicio 5
# Al aplicar al metodo remove en la lista numeros, con la funcion max(), el comando lo que hace es identificar el numero de mayor valor en la lista y luego lo elimina.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# Ejercicio 6
numeros = []
for i in range (10,30 + 1,5):
    numeros.append(i)

print(numeros[0:2])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["Peugeot", "Tesla"]

print(autos)

# Ejercicio 8
dobles = []
for i in range (5,20,5):
    dobles.append(i * 2)

print(dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

# Ejercicio 10
lista_anidada = []
lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([27.5, 57.9, 30.6])
lista_anidada.append(False)
print(lista_anidada)
 

