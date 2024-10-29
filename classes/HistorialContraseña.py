from .Contraseña import Contraseña
from datetime import date

class HistorialContraseña:
    def __init__(self, fechaCambio: date, contraseñaAntigua: str):
        self.fechaCambio = fechaCambio
        self.contraseñaAntigua = contraseñaAntigua

    def registrarCambio(self, contraseña: Contraseña):
        pass

    def mostrarHistorial(self) -> list:
        pass
