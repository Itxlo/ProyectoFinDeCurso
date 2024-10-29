import os
import tkinter as tk
from tkinter import messagebox, StringVar
from database import obtener_categorias, agregar_contraseña, buscar_contraseña, obtener_contraseñas
from database import editar_contraseña, ventana_editar_contraseña, borrar_contraseña
from utils import copiar_al_portapapeles
from security import establecer_contraseña_maestra, validar_contraseña_maestra


def iniciar_interfaz():
    root = tk.Tk()
    root.title("PassKeeper")
    root.geometry("600x400")
    pantalla_inicial(root)
    root.mainloop()


def pantalla_inicial(root):
    if not os.path.exists("password_master.txt"):
        ventana_establecer_contraseña(root)
    else:
        ventana_login(root)


def ventana_establecer_contraseña(root):
    ventana = tk.Toplevel(root)
    ventana.title("Establecer Contraseña Maestra")

    tk.Label(ventana, text="Configura tu contraseña maestra:").pack(pady=5)
    nueva_contraseña = tk.Entry(ventana, show="*", width=30)
    nueva_contraseña.pack(pady=5)

    def guardar_nueva_contraseña():
        establecer_contraseña_maestra(nueva_contraseña.get())
        ventana.destroy()
        messagebox.showinfo("Éxito", "Contraseña maestra establecida.")
        ventana_login(root)

    tk.Button(ventana, text="Guardar", command=guardar_nueva_contraseña).pack(pady=10)


def ventana_login(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Introduce tu contraseña maestra:").pack(pady=10)
    contraseña_maestra = tk.Entry(root, show="*", width=30)
    contraseña_maestra.pack(pady=10)

    def validar_contraseña():
        if validar_contraseña_maestra(contraseña_maestra.get()):
            ventana_principal(root)
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    tk.Button(root, text="Ingresar", command=validar_contraseña).pack(pady=20)


def ventana_principal(root):
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Bienvenido a PassKeeper").pack(pady=10)
    tk.Button(root, text="Añadir Contraseña", command=ventana_agregar_contraseña).pack(pady=10)
    tk.Button(root, text="Ver Contraseñas", command=ventana_ver_contraseñas).pack(pady=10)
    tk.Button(root, text="Buscar Contraseña", command=ventana_buscar_contraseña).pack(pady=10)
    tk.Button(root, text="Salir", command=root.quit).pack(pady=20)



def ventana_agregar_contraseña():
    ventana = tk.Toplevel()
    ventana.title("Añadir Contraseña")

    # Opciones de categorías en el menú desplegable
    tk.Label(ventana, text="Categoría:").pack()
    categoria_var = StringVar(ventana)
    categoria_var.set("Selecciona una categoría")
    categorias = obtener_categorias()
    opciones_menu = tk.OptionMenu(ventana, categoria_var, *categorias)
    opciones_menu.pack(pady=5)

    # Campos para añadir cuenta y contraseña
    tk.Label(ventana, text="Cuenta:").pack()
    cuenta_entry = tk.Entry(ventana, width=30)
    cuenta_entry.pack(pady=5)

    tk.Label(ventana, text="Contraseña:").pack()
    contraseña_entry = tk.Entry(ventana, show="*", width=30)
    contraseña_entry.pack(pady=5)

    def guardar_contraseña():
        cuenta = cuenta_entry.get()
        contraseña = contraseña_entry.get()
        categoria = categoria_var.get()
        if cuenta and contraseña and categoria != "Selecciona una categoría":
            agregar_contraseña(cuenta, contraseña, categoria)
            messagebox.showinfo("Éxito", "Contraseña guardada correctamente.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

    tk.Button(ventana, text="Guardar", command=guardar_contraseña).pack(pady=10)


def ventana_ver_contraseñas():
    ventana = tk.Toplevel()
    ventana.title("Ver Contraseñas")
    tk.Label(ventana, text="Contraseñas almacenadas:").pack(pady=5)

    contraseñas = obtener_contraseñas()

    for cuenta, contraseña, categoria in contraseñas:
        frame = tk.Frame(ventana)
        frame.pack(pady=5)
        tk.Label(frame, text=f"Cuenta: {cuenta}").grid(row=0, column=0, padx=5)
        tk.Label(frame, text=f"Categoría: {categoria}").grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Copiar", command=lambda c=contraseña: copiar_al_portapapeles(c)).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Editar", command=lambda c=cuenta: ventana_editar_contraseña(c)).grid(row=0, column=3, padx=5)
        tk.Button(frame, text="Borrar", command=lambda c=cuenta: borrar_contraseña_confirmacion(c)).grid(row=0, column=4, padx=5)

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

def borrar_contraseña_confirmacion(cuenta):
    respuesta = messagebox.askyesno("Confirmación", f"¿Estás seguro de que deseas borrar la contraseña para {cuenta}?")
    if respuesta:
        borrar_contraseña(cuenta)
        messagebox.showinfo("Éxito", "Contraseña eliminada correctamente.")

def ventana_buscar_contraseña():
    ventana = tk.Toplevel()
    ventana.title("Buscar Contraseña")
    tk.Label(ventana, text="Introduce el nombre de la cuenta a buscar:").pack(pady=5)

    cuenta_entry = tk.Entry(ventana, width=30)
    cuenta_entry.pack(pady=5)

    def buscar():
        cuenta = cuenta_entry.get()
        resultados = buscar_contraseña(cuenta)
        if resultados:
            for widget in ventana.winfo_children():
                widget.destroy()
            tk.Label(ventana, text=f"Resultados para '{cuenta}':").pack(pady=5)
            for res in resultados:
                cuenta, contraseña, categoria = res
                frame = tk.Frame(ventana)
                frame.pack(pady=5)
                tk.Label(frame, text=f"Cuenta: {cuenta}").grid(row=0, column=0)
                tk.Label(frame, text=f"Categoría: {categoria}").grid(row=0, column=1)
                tk.Button(frame, text="Copiar", command=lambda c=contraseña: copiar_al_portapapeles(c)).grid(row=0,
                                                                                                             column=2)
        else:
            messagebox.showinfo("Sin resultados", f"No se encontró ninguna contraseña para '{cuenta}'.")

    tk.Button(ventana, text="Buscar", command=buscar).pack(pady=10)