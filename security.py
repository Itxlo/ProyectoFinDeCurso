import os
from cryptography.fernet import Fernet

# Generar o cargar la clave de encriptación
def generar_clave():
    if not os.path.exists("clave.key"):
        clave = Fernet.generate_key()
        with open("clave.key", "wb") as clave_file:
            clave_file.write(clave)

def cargar_clave():
    return open("clave.key", "rb").read()

# Encriptar y desencriptar contraseñas
def encriptar_contraseña(password):
    clave = cargar_clave()
    f = Fernet(clave)
    return f.encrypt(password.encode())

def desencriptar_contraseña(password_encriptada):
    clave = cargar_clave()
    f = Fernet(clave)
    return f.decrypt(password_encriptada).decode()

# Función para establecer la contraseña maestra
def establecer_contraseña_maestra(contraseña):
    generar_clave()  # Genera la clave si no existe
    contrasena_encriptada = encriptar_contraseña(contraseña)
    with open("password_master.txt", "wb") as file:
        file.write(contrasena_encriptada)

# Función para validar la contraseña maestra ingresada
def validar_contraseña_maestra(entrada):
    try:
        with open("password_master.txt", "rb") as file:
            contrasena_encriptada = file.read()
        contrasena_desencriptada = desencriptar_contraseña(contrasena_encriptada)
        return entrada == contrasena_desencriptada
    except FileNotFoundError:
        return False