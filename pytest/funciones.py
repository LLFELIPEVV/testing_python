def return_3(num: int) -> int:
    return 30 - num

def sum_lista_numeros(lista: list) -> int:
    return sum(lista)

class Persona:
    def __init__(self, nombre, edad) -> None:
        self._nombre = nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre
    
    def get_edad(self):
        return self._edad

def potencia_numeros(num, potencia):
    return num ** potencia

class ErrorCeroDivision(Exception):
    def __str__(self) -> str:
        return "Lo sentimos esta calculadora no puede realizar divisiones por 0"

class Operaciones():
    def __init__(self):
        self._resultado = 0
    
    def get_resultado(self):
        return self._resultado
    
    def set_resultado(self, nuevo_resultado):
        self._resultado = nuevo_resultado
    
    def suma(self, a, b):
        resultado = a + b
        self.set_resultado(resultado)
        
    def resta(self, a, b):
        resultado = a - b
        self.set_resultado(resultado)
    
    def multiplicacion(self, a, b):
        resultado = a * b
        self.set_resultado(resultado)
    
    def division(self, a, b):
        if b == 0:
            raise ErrorCeroDivision
        resultado = a // b
        self.set_resultado(resultado)
