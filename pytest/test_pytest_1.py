import pytest

from funciones import *

# Prueba normal
def test_return_3():
    assert return_3(27) == 3

# Prueba con fixtures
@pytest.fixture
def lista() -> list:
    return [1, 2, 3, 4, 5]

def test_sum_lista_numeros(lista):
    assert sum_lista_numeros(lista) == 15

@pytest.fixture
def persona() -> object:
    return Persona(nombre = "Juan", edad = 30)

def test_persona(persona: object):
    assert persona.get_nombre() == "Juan"
    assert persona.get_edad() == 30

# Prueba con parametrizacion
@pytest.mark.parametrize("num, potencia, resultado", [(1, 9, 1), (4, 8, 65536), (100, 0, 1)])
def test_potencia(num, potencia, resultado):
    assert potencia_numeros(num, potencia) == resultado

@pytest.mark.parametrize("a, b, operacion, resultado", [(2, 4, "suma", 6), (8, 6, "resta", 2), (6, 89, "multiplicacion", 534), (98, 4, "division", 24)])
def test_operaciones(a, b, operacion, resultado):
    self = Operaciones()
    if operacion == "suma":
        self.suma(a, b)
        assert self.get_resultado() == resultado
    elif operacion == "resta":
        self.resta(a, b)
        assert self.get_resultado() == resultado
    elif operacion == "multiplicacion":
        self.multiplicacion(a, b)
        assert self.get_resultado() == resultado
    elif operacion == "division":
        self.division(a, b)
        assert self.get_resultado() == resultado

# Pruebas con marcadores se ejecutan con (pytest pytest -m basicas -v)
@pytest.mark.basicas
def test_suma():
    assert 1 + 1 == 2
    
@pytest.mark.basicas
def test_resta():
    assert 10 - 5 == 5

@pytest.mark.basicas
def test_multiplicacion():
    assert 3 * 6 == 18

@pytest.mark.basicas
def test_division():
    assert 9 / 2 == 4.5
