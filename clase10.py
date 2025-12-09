# feddback
# POO
"""
1 clases - plantillas
    atributos - propiedades
       estaticos
       dinamicos
    metodos - funciones, cosas que realizan el objeto
2 objetos - instancias de las clases - creacion en base a una clase
"""

class Personas:
    tipo = 'humano' # atributo estatico
    def __init__(self, nombre, edad, genero): # metodo constructor
        self.nombre = nombre  # atributo dinamico
        self.edad = edad      # atributo dinamico
        self.genero = genero  # atributo dinamico

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}.')
    def __str__(self):
        return "Personas"
        
persona1 = Personas("cesar",29,"masculino")
persona2 = Personas("Gabriela",29,"femenino")
persona3 = Personas("xavier",29,"masculino")
print(persona1)
persona1.saludar() #ejecutar metodo
persona2.saludar()
persona3.saludar()
print(persona1.nombre, persona1.edad, persona1.genero) # Leer las propiedades del objeto
persona1.nombre = "Carlos" # Modificar las propiedades del objeto
print(persona1.nombre)


#Herencia hereda propiedades y metodos de otra clase
#clase superior padre
#clase hijos
class Animal: #clase padre
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print("hola soy un animal")

class Terrestres(Animal): #clase hija
        def __init__(self, nombre, forma_moverse):
            super().__init__(nombre) #declaro herencia
            self.nombre = nombre
            self.forma_moverse = forma_moverse
        def saludar(self):
            print("hola soy un perro")    

class Acuaticos(Animal): #clase hija
    def __init__(self, nombre, forma_moverse):
        super().__init__(nombre) #declaro herencia
        self.nombre = nombre
        self.forma_moverse = forma_moverse
    def saludar (self):
        print("hola soy un pez")
    
    
animal = Animal("pajaro")
perro =  Terrestres("beagle", "4 patas")
perro.saludar()   
pez= Acuaticos("golden", "aletas")
pez.saludar() 

class A:
    def saludar(self):
        print("saludo desde A")
    
class B:
    def saludar(self):
        print("saludo desde B")
        
class C(A):
    def saludar(self):
        print("saludo desde C")
        
class D(B,A):
    def saludar(self):
        print("saludo desde D")
        
d = D()
d.saludar()
print(D.mro()) #metodo de resolucion de orden
#esto genera un valor genealogico de como funciona los metodos


#Encampsulamiento
#En python todo es publico, encapsular es una herramienta para tratar de proteger las cosas
# Privado => para manipular debo ser consciente y solo lo puedo hacer desde la clase
# Protegido => es una sintaxis que me indica que no deberia de tocar los datos
# publico => cualquiera puede acceder

class Persona:
    def __init__(self, nombre, edad, cedula, salario):
        self.nombre = nombre
        self.edad = edad
        self.__cedula = cedula # privado usa doble guion bajo
        self._salario = salario #se coloca un guion bajo para indicar que es protegido
    def informacion(self):
        print(self.__cedula)
    def get_cedula(self): #para leer u obtener el valor privado
        return self.__cedula
    def set_cedula(self, cedula): #modificar el valor
        self.__cedula = cedula

        
persona1 = Persona("Cesar", 28, "1234567890", 5000)
print(persona1.nombre)

persona1.nombre = "gabriela"
print(persona1.nombre)
print(persona1._salario)
persona1._salario = "4000"
print(persona1._salario)
print(persona1.get_cedula())
persona1.set_cedula("0926032236")
print(persona1.get_cedula())


#Polimorfismo muchas formas que un metodo o una accion hace cosas diferentes
class Vehiculo:
    def mover(self):
        pass  # La clase base no tiene una implementación de mover, es abstracto

class Coche(Vehiculo):
    def mover(self):
        return "El coche se mueve a gran velocidad."

class Bicicleta(Vehiculo):
    def mover(self):
        return "La bicicleta se mueve pedaleando."

def hacer_mover(vehiculo):
    print(vehiculo.mover())

# Crear objetos de Coche y Bicicleta
coche = Coche()
bicicleta = Bicicleta()

# Llamar a la función hacer_mover con diferentes objetos
hacer_mover(coche)      # Se espera el mensaje del coche
hacer_mover(bicicleta)  # Se espera el mensaje de la bicicleta



#Abstraccion
from abc import ABC, abstractmethod

class Auto(ABC): #boceto o guia
    llantas = 4
    @abstractmethod
    def encender(self):
        pass

class Mercedes(Auto): #plantilla original
        def __init__(self, color):
            self.color =color
        def encender(self):
            print("encendio el mercedes")

auto1 = Mercedes("negro")            