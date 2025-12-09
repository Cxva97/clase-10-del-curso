#Ejercicios
# Ejercicio 1
# Crear una clase padre de que vehiculos
# con los atributos numero_ruedas y tipo terrestre o acuatico
# crear una subclase de auto que hereda de vehiculo y aparte tiene atributos de marca, modelo y color
# crear un metodo para el auto encender, acelerar, apagar
# crear una subclase de moto que herede de vehiculo y aparte tiene atributo marca, modelo y color
# crear un metodo para la moto encender, acelerar, apagar
# crear 2 autos y 2 motos
class Vehiculo:
    def __init__(self, numero_ruedas, tipo):
        self.numero_ruedas = numero_ruedas
        self.tipo = tipo
        
class Auto(Vehiculo):
    def __init__(self, numero_ruedas, tipo, marca, modelo, color):
        super().__init__(numero_ruedas, tipo)
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def encender(self):
        return f"El auto {self.marca} {self.modelo} está encendido."
    
    def acelerar(self):
        return f"El auto {self.marca} {self.modelo} está acelerando."
    
    def apagar(self):
        return f"El auto {self.marca} {self.modelo} está apagado."
    
class Moto(Vehiculo):
    def __init__(self, numero_ruedas, tipo, marca, modelo, color):
        super().__init__(numero_ruedas, tipo)
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def encender(self):
        return f"La moto {self.marca} {self.modelo} está encendida."
    
    def acelerar(self):
        return f"La moto {self.marca} {self.modelo} está acelerando."
    
    def apagar(self):
        return f"La moto {self.marca} {self.modelo} está apagada."
    
auto1 = Auto(4, "terrestre", "Toyota", "Corolla", "Rojo")
auto2 = Auto(4, "terrestre", "Honda", "Civic", "Azul")
moto1 = Moto(2, "terrestre", "Yamaha", "YZF-R3", "Negra")
moto2 = Moto(2, "terrestre", "Kawasaki", "Ninja 400", "Verde")  
print(auto1.encender())
print(moto1.acelerar()) 
print(moto2.apagar())
print(auto2.acelerar())

# Ejercicio 2: Sistema de Biblioteca Básico
# Crear un sistema de biblioteca que incluya:
# Clase Libro con atributos estáticos (como tasa_multa = 0.2) y dinámicos (como título, autor)
# Métodos para calcular multa por días de retraso
# Herencia para crear una clase LibroDigital que añada atributos específicos(formato) y un metodo que diga descargar
# muestra el estado descargado o disponible.
# crear 1 libro de cada tipo
# imprimir un mensaje con el nombre y la multa de 2 dias

class Libro:
    tasa_multa = 0.2
    def __init__(self, titulo, autor):
        self.autor = autor
        self.titulo = titulo
    def calcular_multa(self, dias):
        return dias * self.tasa_multa
    
class LibroDigital(Libro): #hereda de libro
    def __init__ (self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato
        self.estado = True #True disponible, False descargado
        
    def verificar_estado(self):
        if self.estado:
            print("libro disponible")
        else:
            print("libro descargado")
            
libro1 = Libro("Cien años de soledad", "Gabriel Garcia Marquez")
libro2 = LibroDigital("1984", "George Orwell", "PDF")
print(f"El libro {libro1.titulo} tiene una multa de {libro1.calcular_multa(2)} por 2 dias de retraso. ")   

 # Ejercicio 3: Sistema de Formas Geométricas
# Objetivo:
# Calcular áreas y perímetros de formas geométricas usando:
# Abstracción: Clase abstracta Forma con métodos abstractos.
# Polimorfismo: Cada forma (Circulo, Rectangulo) calcula su área/perímetro diferente.
# Encapsulamiento: Atributos como radio o base son protegidos.
# Requisitos:
# Clase abstracta Forma:
# Métodos abstractos: calcular_area(), calcular_perimetro().
# Clases concretas:
# Circulo: Atributo _radio, implementa métodos con fórmulas π*r² y 2πr.
# Rectangulo: Atributos _base y _altura, implementa métodos con fórmulas base*altura y 2*(base+altura).

from abc import ABC, abstractmethod
import math
class Forma(ABC):
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self._radio = radio
    def perimetro(self):
        return 2 * math.pi*self._radio
    def area(self):
        return math.pi * (self._radio**2)
    
class Rectangulo(Forma):
    def __init__(self, base, altura):
        self._base = base
        self.altura = altura
    def perimetro(self):
        return 2*(self._base + self.altura)
    def area(self):
        return self._base * self.altura
    
circulo1 = Circulo(4)
rectangulo1 = Rectangulo(2,4)
print(f"El perimetro del circulo es: {circulo1.perimetro()}")  
print(f"El area del circulo es: {circulo1.area()}")
print(f"El perimetro del rectangulo es: {rectangulo1.perimetro()}")
print(f"El area del rectangulo es: {rectangulo1.area()}") 


"""Crea una clase CuentaBancaria que implemente los siguientes requisitos:
Debe tener un saldo inicial que se establece al crear la cuenta
Debe proteger el acceso directo al saldo (atributo protegido)
Debe tener un PIN privado para autorizar operaciones
Debe permitir depositar dinero (solo cantidades positivas)
Debe permitir retirar dinero solo si se proporciona el PIN correcto y hay saldo suficiente
Debe incluir un método privado para verificar el PIN
Debe proporcionar un método público para consultar el saldo de forma controlada
Restricciones importantes:
No se debe permitir el acceso directo al PIN desde fuera de la clase
El saldo no debería ser modificable directamente desde fuera de la clase
Las retiradas de dinero deben estar protegidas por verificación de PIN"""
