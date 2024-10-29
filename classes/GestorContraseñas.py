from .Contraseña import Contraseña

class GestorContraseñas:
    def __init__(self):
        self.contraseñas = []

    def añadirContraseña(self, contraseña: Contraseña):
        pass

    def editarContraseña(self, contraseña: Contraseña):
        pass

    def eliminarContraseña(self, contraseña: Contraseña):
        pass

    def buscarContraseña(self, nombreServicio: str) -> Contraseña:
        pass

    def visualizarContraseñas(self) -> list:
        pass

    def clasificarContraseñas(self, categoria: str) -> list:
        pass
