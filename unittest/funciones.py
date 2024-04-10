from conexion_BD import inicializar_base_datos

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

class BD:
    def __init__(self) -> None:
        self.con = inicializar_base_datos()
    
    def __del__(self) -> None:
        self.con.close()
    
    def crear_usuario(self, nombre: str, email: str):
        self.con.execute('INSERT INTO usuarios (nombre, email) VALUES (?, ?)', (nombre, email))
        self.con.commit()

    def get_usuario(self, id:int=None, nombre:str=None, email:str=None):
        consulta = 'SELECT * FROM usuarios WHERE'
        parametros = []
        if id is not None:
            consulta += ' id = ?'
            parametros.append(id)
        if nombre is not None:
            consulta += ' nombre = ?'
            parametros.append(nombre)
        if email is not None:
            consulta += ' email = ?'
            parametros.append(email)
        cursor = self.con.execute(consulta, parametros)
        usuario = cursor.fetchone()
        if usuario:
            # Convertir la tupla a un diccionario
            usuario_dict = {'id': usuario[0], 'nombre': usuario[1], 'email': usuario[2]}
            return usuario_dict
        else:
            return None

class GestorDeEstudiantes:
    def __init__(self):
        self.estudiantes = []
    
    def add_estudiantes(self, Nombre: str, Edad: int) -> None:
        self.estudiantes.append({'Nombre': Nombre, 'Edad': Edad})
    
    def del_estudiantes(self, Nombre: str) -> None:
        for estudiante in self.estudiantes:
            if estudiante['Nombre'] == Nombre:
                self.estudiantes.remove(estudiante)
    
    def get_listado_estudiantes(self) -> list:
        return self.estudiantes.copy()
    
    def get_estudiante(self, Nombre: str) -> dict:
        for estudiante in self.estudiantes:
            if estudiante['Nombre'] == Nombre:
                return estudiante
    