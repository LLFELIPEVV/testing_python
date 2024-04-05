def suma(num1: int, num2: int) -> int:
    return num1 + num2

def cadenas(cadena1: str, cadena2: str) -> str:
    return f"{cadena1} {cadena2}"

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n*factorial(n-1)
    