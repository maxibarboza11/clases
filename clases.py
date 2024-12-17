#SCRIP DE ESTRUCUTURA DE UNA CLASE (class)

#Esta clase es programacion orientada a objetos
#el paradigma orientado a objeto, la idea a que todo lo que gobierna la realidad se puede
#reproducir con programacion orientada a objetos, se dice que todos estos objetos cuando se 
#agrupan, se llaman clase, cada clase tiene sus atributos.

#como defino ojetos? para definir el molde o la clase es como sigue:
import random
class Persona:
    def __init__(self, nombre, edad, ciudad):#init es el constructor al que le paso una 
#serie de parametros, che vos clase persona vas a tener estos tres atributos y con estos 
#valores que defino a continuacion:


#por convencion se usa self y se lee a mi mismo me atribuyo los siguientes atributos
#init me inicializa la clase
#todas las funciones que esten en una clase se las van a conocer como métodos
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
         
        self.p1 = [random.randint(0,20) for x in range(0,5)]
        self.p2 = [random.randint(0,20) for x in range(0,5)]
        self.p3 = [random.randint(0,20) for x in range(0,5)] 
    def presentarse(self): 
        return f'Hola soy {self.nombre}, tengo {self.edad} y vivo en {self.ciudad}'
        
    def mayor(self):
       # print(self.edad>17)
        return self.edad>17
    
    def cambiarciudad(self,nuevaciudad):
        self.ciudad = nuevaciudad
        
    def numeros(self):
        num = [random.randint(0,100) for x in range(0,5)]
        return  num 
    
#que  tenia que hacer la siguiente esta funcion  ?  
"""def ruleta(self):
        while contenido==false: 
            contenido=all(elem in self.)"""

#Para Probar la clase
"""persona1= Persona('Maxi',24,'Salta')
print(persona1.presentarse())
print(persona1.nombre)
print(persona1.mayor())
"""
#Añadir metodo que permita cambiar la ciudad de una persona
"""persona1.cambiarciudad(input('igrese nueva ciudad: '))
print(persona1.presentarse()) """ 

#Añadir un atributo numeros que almacene 5 numeros enteros aleatorios
"""print(persona1.numeros())
"""

#En el programa principal genere 3 objetos persona
persona1 = Persona("Maxi", 19 , "Salta")
persona2 = Persona("Lucas", 32 , "Rosario de Lerma")
persona3 = Persona("Pedro", 12 , "Campo Quijano")

  
#En el programa principal genere una lista de numeros aleatorios mientras no ocurra que 
#todos los numeros de al menos una persona esten contenidos en dicha lista

print (f"numeros de p1: {persona1.numeros()}")
print (f"numeros de p2: {persona1.numeros()}")
print (f"numeros de p3: {persona1.numeros()}")


    
"""control =  True    
while control:      
    lista = [] 
    for x in lista:
        if x == persona1.numeros()
        lista.append(random.randint(0,100))
        print(lista)
        print(random.randint(0,100))"""
lista1 = persona1.numeros() 
print(lista1[0])
print (f"numeros de p1: {persona1.numeros()}")

#Despues agregar la condicion de que no se repitan los valores