from layer import Capa
import numpy as np

class CapaConectada(Capa):

    def __init__(self, entrada_size, salida_size):
        self.pesos = np.random.rand(entrada_size, salida_size) - 0.5
        self.sesgo = np.random.rand(1, salida_size) - 0.5

    def propagacion(self, datos_entada):
        self.entrada = datos_entada
        self.salida = np.dot(self.entrada, self.pesos) + self.sesgo
        return self.salida

    def retropropagacion(self, error_salida, ritmo_aprendizaje):
        error_entrada = np.dot(error_salida, self.pesos.T)
        error_pesos = np.dot(self.entrada.T, error_salida)

        self.pesos -= ritmo_aprendizaje * error_pesos
        self.sesgo -= ritmo_aprendizaje * error_salida
        return error_entrada