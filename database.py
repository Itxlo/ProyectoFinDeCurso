import sqlite3
from security import desencriptar_contraseña, encriptar_contraseña

# Conectar a la base de datos
def conectar_db():
    return sqlite3.connect("passwords.db")

# Crear la tabla si no existe
def crear_tabla():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contraseñas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cuenta TEXT NOT NULL,
                contraseña TEXT NOT NULL,
                categoria TEXT NOT NULL
            )
        """)
        conn.commit()

def agregar_contraseña(cuenta, contraseña, categoria):
    contraseña_encriptada = encriptar_contraseña(contraseña)  # Encriptar la contraseña antes de guardarla
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contraseñas (cuenta, contraseña, categoria)
            VALUES (?, ?, ?)
        """, (cuenta, contraseña_encriptada, categoria))
        conn.commit()

def buscar_contraseña(cuenta):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT cuenta, contraseña, categoria FROM contraseñas WHERE cuenta=?", (cuenta,))
        resultados = cursor.fetchall()
        return [(r[0], desencriptar_contraseña(r[1]), r[2]) for r in resultados]  # Desencriptar la contraseña antes de retornarla

def obtener_categorias():
    # Ejemplo de cómo obtener categorías. Puede ser mejorado según tu lógica
    return ["Personal", "Trabajo", "Estudio"]

def obtener_contraseñas():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT cuenta, contraseña, categoria FROM contraseñas")
        resultados = cursor.fetchall()
        return [(r[0], desencriptar_contraseña(r[1]), r[2]) for r in resultados]  # Desencriptar las contraseñas

# Asegúrate de crear la tabla al iniciar
crear_tabla()
