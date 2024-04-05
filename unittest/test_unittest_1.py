import unittest
from funciones import *

class TestFunciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(300, 90), 390)
        self.assertEqual(suma(130.5, 4.04), 134.54)
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)
    
    def test_cadenas(self):
        self.assertEqual(cadenas("Hola", "mundo"), "Hola mundo")
        self.assertEqual(cadenas("Hola", "mucho gusto"), "Hola mucho gusto")
        self.assertEqual(cadenas("", ""), " ")
    
    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
    
    def test_add_list(self):
        lista = []
        add_list(lista, 5)
        add_list(lista, 2)
        add_list(lista, "dfksadk")
        add_list(lista, [15, 60, 29])
        add_list(lista, 50)
        
        self.assertEqual(lista[-1], 50)
        self.assertEqual(len(lista), 5)

class TestPersona(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.persona = Persona("Juan")
    
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.persona
    
    def test_get_nombre(self):
        self.assertEqual(self.persona.get_nombre(), "Juan")
    
    def test_set_nombre(self):
        self.persona.set_nombre("Pedro")
        self.assertEqual(self.persona.get_nombre(), "Pedro")

class TestCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        self.calculadora = Calculadora()
    
    def test_sumar(self):
        self.calculadora.sumar(5, 8)
        self.assertEqual(self.calculadora.get_resultado(), 13)
    
    def test_restar(self):
        self.calculadora.restar(10, 2)
        self.assertEqual(self.calculadora.get_resultado(), 8)

if __name__ == '__main__':
    unittest.main()
