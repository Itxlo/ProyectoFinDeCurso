class Contraseña:
    def __init__(self, valor: str, servicio: str, categoria: str, fuerza: str):
        self.valor = valor
        self.servicio = servicio
        self.categoria = categoria
        self.fuerza = fuerza

    def esFuerte(self) -> bool:
        pass

    def actualizarContraseña(self, nuevaContraseña: str):
        pass

    def eliminarContraseña(self):
        pass
