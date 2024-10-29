from gui import iniciar_interfaz
#from database import conectar_db
from security import generar_clave


def main():
    # Crear la clave de encriptación si no existe
    generar_clave()

    # Crear la base de datos y las tablas necesarias si no existen
    #conectar_bd()

    # Iniciar la interfaz gráfica de la aplicación
    iniciar_interfaz()


if __name__ == "__main__":
    main()
