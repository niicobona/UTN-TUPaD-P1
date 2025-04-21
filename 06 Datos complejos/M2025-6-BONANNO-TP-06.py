# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = "1200"
precios_frutas["Manzana"] = "1500"
precios_frutas["Pera"] = "2300"
print(precios_frutas)

# Ejercicio 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = "1200"
precios_frutas["Manzana"] = "1500"
precios_frutas["Pera"] = "2300"
# CAMBIO DE PRECIOS...
precios_frutas["Banana"] = "1330"
precios_frutas["Manzana"] = "1700"
precios_frutas["Melón"] = "2800"
print(precios_frutas)

# Ejercicio 3
precios_frutas = {'Banana': '1330', 'Ananá': 2500, 'Melón': '2800', 'Uva': 1450, 'Naranja': '1200', 'Manzana': '1700', 'Pera': '2300'}
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# Ejercicio 4
class Persona :
    def __init__(self,nombre,pais,edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad
    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
persona = Persona("Nicolas","Argentina",33)
persona.saludar()

# Ejercicio 5
import math as mt
class Circulo :
    def __init__(self,radio):
        self.radio = radio
    def calcular_area(self):
        area = 2*mt.pi*self.radio
        print(f"El area del circulo es {area}")
    def calcular_perimtetro(self):
        perimetro = mt.pi*(self.radio**2)
        print(f"El area del circulo es {perimetro}") 
circulo = Circulo(6)   
circulo.calcular_area()
circulo.calcular_perimtetro()    

# Ejercicio 6
class Balanceo:

    def __init__(self, expresion):
        self.expresion = expresion
        self.pila = []
        self.pares = {')': '(', '}': '{', ']': '['}

    def esta_balanceada(self):
        for caracter in self.expresion:
            if caracter in "({[":
                self.pila.append(caracter)
            elif caracter in ")}]":
                if not self.pila or self.pila[-1] != self.pares[caracter]:
                    return False
                self.pila.pop()
        return not self.pila 
    
expresion1 = Balanceo("({[]})")
print(expresion1.esta_balanceada()) 

expresion2 = Balanceo("({[})")
print(expresion2.esta_balanceada())

# Ejercicio 7
from collections import deque

class Cola:
    def __init__(self):
        self.cola = deque()

    def agregar(self, cliente):
        self.cola.append(cliente) 
        print(f"cliente {cliente}, agregado a la cola.")

    def atender(self):
        if self.cola:
            cliente = self.cola.popleft()
            print(f"Atendiendo al cliente {cliente}")
        else:
            print("No hay gente en la cola para atender.")

    def siguiente_cliente(self):
        if self.cola:
            print(f"Siguiente cliente: {self.cola[0]}")
        else:
            print("No hay clientes en espera.")


banco = Cola ()
banco.agregar("Nicolas")
banco.agregar("Juan")
banco.agregar("Pedro")

banco.siguiente_cliente()

banco.atender()
banco.siguiente_cliente()
banco.atender()
banco.atender()
banco.siguiente_cliente()

# Ejercicio 8
class Nodo:
    def __init__(self, producto):
        self.producto = producto 
        self.siguiente = None 

class ListaEnlazada:
    def __init__(self):
        self.lista = None  

    def agregarProducto(self, producto):
        nuevo_nodo = Nodo(producto)
        nuevo_nodo.siguiente = self.lista
        self.lista = nuevo_nodo

    def listaSupermercado(self):
        actual = self.lista
        while actual:
            print(actual.producto, end=" , ")
            actual = actual.siguiente
        print("siguiente...")

lista = ListaEnlazada()
lista.agregarProducto("Leche")
lista.agregarProducto("Pan")
lista.agregarProducto("Fideos")
lista.agregarProducto("Carne")
lista.listaSupermercado()

# Ejercicio 9
class Nodo:
    def __init__(self, dato):
        self.dato = dato 
        self.siguiente = None  

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrarListaNormal(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' --> ')
            actual = actual.siguiente
        print("None")

    def invertir(self):
        anterior = None
        actual = self.cabeza

        while actual:
            siguiente = actual.siguiente      
            actual.siguiente = anterior   
            anterior = actual                
            actual = siguiente             

        self.cabeza = anterior 

lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
print("Lista normal:")
lista.mostrarListaNormal()
lista.invertir()
print("Lista invertida:")
lista.mostrarListaNormal()