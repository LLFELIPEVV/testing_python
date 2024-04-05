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

if __name__ == '__main__':
    unittest.main()
