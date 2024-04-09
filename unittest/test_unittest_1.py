import unittest

from funciones import *
from conexion_BD import inicializar_base_datos

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

class TestBD(unittest.TestCase):
    def setUp(self) -> None:
        self.BD = BD()

    def test_crear_usuario(self):
        self.BD.crear_usuario("Pedro", "pedro123@gmail.com")
        usuario = self.BD.get_usuario(nombre="Pedro")
        self.assertIsNotNone(usuario)  # Verifica que se haya encontrado un usuario
        self.assertEqual(usuario['nombre'], "Pedro")
        self.assertEqual(usuario['email'], "pedro123@gmail.com")
    
class TestGestorEstudiantes(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.Gestor = GestorDeEstudiantes()
        cls.Gestor.add_estudiantes("Pedro", 10)
        cls.Gestor.add_estudiantes("Maria", 40)
    
    def test_add_estudiantes(self):
        self.Gestor.add_estudiantes("Juan", 20)
        self.assertEqual(len(self.Gestor.get_listado_estudiantes()), 3)
    
    def test_del_estudiantes(self):
        self.Gestor.del_estudiantes("Juan")
        self.assertEqual(len(self.Gestor.get_listado_estudiantes()), 3)
        estudiante = self.Gestor.get_estudiante("Juan")
        self.assertIsNone(estudiante)
    
    def test_get_estudiante(self):
        usuario = self.Gestor.get_estudiante("Pedro")
        self.assertEqual(usuario.Name, "Pedro")
        self.assertEqual(usuario.Edad, 10)

    def test_get_listado_estudiantes(self):
        listado = self.Gestor.get_listado_estudiantes()
        self.assertEqual(len(listado), 2)
        self.assertIn({'Nombre': "Pedro", 'Edad': 10}, listado)
        self.assertIn({'Nombre': "Maria", 'Edad': 40}, listado)
        #self.assertIn({'Nombre': "Juan", 'Edad': 20}, listado)

if __name__ == '__main__':
    unittest.main()
