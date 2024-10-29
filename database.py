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
        filas = cursor.fetchall()

    # Desencriptar cada contraseña antes de retornarla
    contraseñas_desencriptadas = [(cuenta, desencriptar_contraseña(contraseña), categoria) for cuenta, contraseña, categoria in filas]
    return contraseñas_desencriptadas
def ventana_editar_contraseña(cuenta):
    ventana = tk.Toplevel()
    ventana.title(f"Editar Contraseña: {cuenta}")
    tk.Label(ventana, text="Nueva Contraseña:").pack()
    nueva_contraseña_entry = tk.Entry(ventana, show="*", width=30)
    nueva_contraseña_entry.pack(pady=5)

    def guardar_cambios():
        nueva_contraseña = nueva_contraseña_entry.get()
        if nueva_contraseña:
            editar_contraseña(cuenta, nueva_contraseña)
            messagebox.showinfo("Éxito", "Contraseña actualizada correctamente.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "La contraseña no puede estar vacía.")

    tk.Button(ventana, text="Guardar Cambios", command=guardar_cambios).pack(pady=10)


def borrar_contraseña(cuenta):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contraseñas WHERE cuenta=?", (cuenta,))
        conn.commit()



def editar_contraseña(cuenta, nueva_contraseña):
    nueva_contraseña_encriptada = encriptar_contraseña(nueva_contraseña)
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE contraseñas SET contraseña=? WHERE cuenta=?", (nueva_contraseña_encriptada, cuenta))
        conn.commit()

crear_tabla()