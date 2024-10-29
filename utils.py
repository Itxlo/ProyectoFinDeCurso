import pyperclip

# utils.py
import tkinter as tk

def copiar_al_portapapeles(texto):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana de Tkinter
    root.clipboard_clear()  # Limpia el portapapeles
    root.clipboard_append(texto)  # Copia el texto al portapapeles
    root.update()  # Actualiza el portapapeles
    root.destroy()  # Cierra la ventana oculta
