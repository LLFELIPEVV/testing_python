def suma(num1: int, num2: int) -> int:
    return num1 + num2

def cadenas(cadena1: str, cadena2: str) -> str:
    return f"{cadena1} {cadena2}"

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n*factorial(n-1)

def add_list(lista: list, elem: any) -> None:
    lista.append(elem)

class Persona:
    def __init__(self: object, nombre: str) -> None:
        self._nombre = nombre
    
    def get_nombre(self: object) -> str:
        return self._nombre
    
    def set_nombre(self: object, nuevo_nombre: str) -> None:
        self._nombre = nuevo_nombre

class Calculadora:
    def __init__(self) -> None:
        self._resultado = 0
    
    def sumar(self, num1, num2):
        self._resultado = num1 + num2
    
    def restar(self, num1, num2):
        self._resultado = num1 - num2
    
    def get_resultado(self):
        return self._resultado