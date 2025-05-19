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

num_fibo=int(input("Ingrese el valor de la serie Fibonacci: "))
for i in range(0,num_fibo + 1):
    print(f"El valor de la serie {i} de Fibonacci es: {fibonacci(i)}")

# EJERCICIO 3 
def potencia_num(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia_num(n,m-1)
    
base=int(input("Ingrese la base: ")) 
exponente=int(input("Ingrese el exponente: "))
resultado = potencia_num(base,exponente)
print(f"{base}^{exponente}={resultado}")

# EJERCICIO 4
num_decimal=int(input("Ingrese un numero entero positivo en base decimal: "))
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return  decimal_a_binario(numero // 2) + str(numero % 2)
        
print(decimal_a_binario(num_decimal))

# EJERCICIO 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    return False

texto = input("Ingrese una palabra: ")
print(es_palindromo(texto))

# EJERCICIO 6
def suma_digitos (n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
num = int(input("Ingrese un numero positivo: "))
print(f"La suma de las cifras del numero ingresado es de: {suma_digitos(num)}")

# EJERCICIO 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
n_bloques = int(input("Ingrese la base de bloques: "))
print(f"El total de bloques necesarios para construir la pirámide es de {contar_bloques(n_bloques)}")

# EJERCICIO 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero//10,digito)
    else:
        return contar_digito(numero//10,digito)  
numero = int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese el digito que desea buscar entre 0 y 9: "))
print(f"El {digito} aparece {contar_digito(numero,digito)} veces")