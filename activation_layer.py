from layer import Capa

class CapaDeActivacion(Capa):
    def __init__(self, activacion, activacion_prima):
        self.activacion = activacion
        self.activacion_prima = activacion_prima

    def propagacion(self, datos_entrada):
        self.entrada = datos_entrada
        self.salida = self.activacion(self.entrada)
        return self.salida

    def retropropagacion(self, error_salida, ritmo_aprendizaje):
        return self.activacion_prima(self.entrada) * error_salida