import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mi Aplicación Tkinter")
root.geometry("400x300")  # Define el tamaño de la ventana

# Ejemplo de un widget simple (como un botón o una etiqueta)
label = tk.Label(root, text="¡HOLA SOY PABLO!")
label.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()