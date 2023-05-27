import numpy as np

from network import Red
from fully_connected_layer import CapaConectada
from activation_layer import CapaDeActivacion
from activation import tanh, tanh_prime
from loss import mse, mse_prime

if __name__=="__main__": 
    x_train = np.array([[[0, 0]], [[0, 1]], [[1, 0]], [[1, 1]]])
    y_train  =np.array([[[0]], [[1]], [[1]], [[0]]])

    net = Red()
    net.nueva_capa(CapaConectada(2, 3))
    net.nueva_capa(CapaDeActivacion(tanh, tanh_prime))
    net.nueva_capa(CapaConectada(3, 1))
    net.nueva_capa(CapaDeActivacion(tanh, tanh_prime))

    #Train 
    net.usar(mse, mse_prime)
    net.ajustar(x_entrenamiento=x_train, y_entrenamiento=y_train, iteraciones=1000, ritmo_aprendizaje=0.1)

    #Test
    out = net.predecir(x_train)
    print(out)
