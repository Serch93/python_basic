#variables

name = "Arturo"
namePerson = 5

#Tipos de Datos
string = 'python'
inter = 9

print(string)
print(string + str(inter))


float = 55.8999884548
print(type(float))


#formato

print("My text {:d}".format(inter))

string = "Mi nombre es {name} y tengo un {what}".format(
    name = "Sergio",
    what = "Curso"
)
print(string)

# lista

lista = [5,6,7,8,11,-5,50]
print(lista[6])

del lista[6]
print(lista)

lista.append('string')
print(lista)

lista.remove(7)
print(lista)

#condicionales

entero = 10
nombre = "Sebas"

#condicional

if entero == 10 or nombre == "Res":
    print("Hola Mundo")
else:
    print("Incorrecto")
    
# for

nombres = ["Omar","Arturo","Vicente","Alondra","Carla"]

for n in nombres:
    print(n)

#Funciones

def sum(a,b):
    print("Hola soy una funcion")
    return a+b    

def imprimir(number):
    print(number)
    
imprimir(sum(10,14))

# Clases

class Puerta:
    abierta = True
    material = "madera"
    alto = 200
    ancho = 10
    largo = 100
    
    def __init__(self,abierta,material):
        self.abierta = abierta
        self.material = material
    
    def volumen(self):
        return self.alto * self.ancho * self.largo
    
puerta = Puerta(False,"acero")
print(puerta.material)
print(puerta.volumen())

#Enum
#from enum import Enum

class Color():
    RED = 1
    BLUE = 2
    BLACK = 3
    
print(Color.RED)
    
#Diccionarios

persona = {'nombre' : 'Andres', 'edad' : 29, 'curso' : ['vue','Django'] }

print(persona['curso'])

#Errores y excepciones
try:
    int('Sergio')
except:
    print('Ocurrio error con el proceso')

print('Fin de la app XD')