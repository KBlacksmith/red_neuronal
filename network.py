class Red: 
    def __init__(self) -> None:
        self.capas = []
        self.perdida = None
        self.perdida_prima = None

    def nueva_capa(self, capa): 
        self.capas.append(capa)

    def usar(self, perdida, perdida_prima):
        self.perdida = perdida
        self.perdida_prima = perdida_prima

    def predecir(self, datos_entrada): 
        muestras = len(datos_entrada)
        resultados = []

        for i in range(muestras): 

            salida = datos_entrada[i]
            for capa in self.capas: 
                salida = capa.propagacion(salida)
            resultados.append(salida)
        return resultados
    
    def ajustar(self, x_entrenamiento, y_entrenamiento, iteraciones, ritmo_aprendizaje): 
        muestras = len(x_entrenamiento)

        for i in range(iteraciones): 
            err = 0
            for j in range(muestras): 
                salida = x_entrenamiento[j]

                for capa in self.capas: 
                    salida = capa.propagacion(salida)
                
                err += self.perdida(y_entrenamiento[j], salida)

                error = self.perdida_prima(y_entrenamiento[j], salida)

                for capa in reversed(self.capas): 
                    error = capa.retropropagacion(error, ritmo_aprendizaje)
            
            err /= muestras
            print('Iteracion %d/%d     error=%f' % (i + 1, iteraciones, err))
