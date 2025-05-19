# EJERCICIO 1
def num_factorial(num):
    if num == 0 :
        return 1
    else:
        return num * num_factorial(num-1)

num= int(input("Ingrese un numero positvo: "))
for i in range (1,num + 1):
    print (f"El factorial de {i} es: {num_factorial(i)}")

# EJERCICIO 2
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

print(fibonacci(4))