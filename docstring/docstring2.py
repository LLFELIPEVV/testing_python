import math

def suma(a: int, b: int) -> int:
    """Suma dos numeros y devuelve el resultado

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: La suma de a y b.
    """
    return a + b

def factorial(n: int) -> int:
    """Calcula el factorial de un número

    Args:
        n (int): Número entero.

    Returns:
        int: Factorial de n.
    """
    
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def maximo(lista: list) -> int:
    """Encuentra el valor maximo de una lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        int: Valor maximo de la lista.
    """
    
    return max(lista)

def contar_letra(cadena: str, letra: str) -> int:
    """Cuenta la cantidad de veces que aparece una letra en una cadena.

    Args:
        cadena (str): Cadena de texto.
        letra (str): Letra a contar.

    Returns:
        int: Cantidad de veces que aparece la letra en la cadena.
    """
    
    return cadena.lower().count(letra)

def promedio(lista: list) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista (list): Lista de números.

    Returns:
        float: Promedio de los números en la lista.
    """
    
    return sum(lista) / len(lista)

def eliminar_duplicados(lista: list) -> list:
    """Elimina elementos duplicados de una lista.

    Args:
        lista (list): Lista con elementos duplicados.

    Returns:
        list: Lista sin elementos duplicados.
    """
    
    return sorted(list(set(lista)))

def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte una temperatura de Celsius a Fahrenheit.

    Args:
        celsius (float): Temperatura en grados Celsius.

    Returns:
        float: Temperatura en grados Fahrenheit.
    """
    
    return (celsius * 9/5) + 32

def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado su radio.

    Args:
        radio (float): Radio del círculo.

    Returns:
        float: Área del círculo.
    """
    
    return math.pi * radio ** 2

def es_primo(n: int) -> bool:
    """Verifica si un número dado es primo.

    Args:
        n (int): Número entero.

    Returns:
        bool: True si es primo, False de lo contrario.
    """
    
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        return True

def es_palindromo(cadena: str) -> bool:
    """Verifica si una cadena es un palíndromo.

    Args:
        cadena (str): Cadena de texto.

    Returns:
        bool: True si es un palíndromo, False de lo contrario.
    """
    
    return cadena.lower() == cadena[::-1].lower()