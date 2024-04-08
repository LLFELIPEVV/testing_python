import sqlite3
# Función que crea la estructura de la base de datos
def inicializar_base_datos():
    conn = sqlite3.connect(':memory:')  # Usamos una base de datos en memoria para las pruebas
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)')
    conn.commit()
    return conn
