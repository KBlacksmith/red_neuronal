class Capa:
    def __init__(self):
        self.entrada = None
        self.salida = None

    def propagacion(self, entrada):
        raise NotImplementedError

    def retropropagacion(self, error_salida, ritmo_aprendizaje):
        raise NotImplementedError