"""Definición dde la red neuronal """
import numpy as np

class NeuralNetwork:
    """Pesos (weights_input_hidden y weights_hidden_output): Son matrices que conectan las capas de la red. 
    En este caso, conectan la capa de entrada con la capa oculta, y la capa oculta con la capa de salida. 
    Los pesos son los "genes" que se optimizan y evolucionan."""

    def __init__(self, input_size, hidden_size, output_size):
        """
        NumPy genera una matriz de números aleatorios que siguen una distribución normal estándar
        
        Por lo tanto, si, por ejemplo, input_size es 3 y hidden_size es 2, la llamada a np.random.randn(3, 2) 
        generará una matriz de 3 filas y 2 columnas con valores aleatorios,
        """
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)

    """
    Esta función realiza la propagación hacia adelante (forward propagation), es decir, el cálculo que convierte las entradas en salidas.
    """
    def forward(self, inputs):
        hidden_layer = np.dot(inputs, self.weights_input_hidden)
        hidden_layer = self.sigmoid(hidden_layer)
        
        output_layer = np.dot(hidden_layer, self.weights_hidden_output)
        output_layer = self.sigmoid(output_layer)
        
        return output_layer

    """Función sigmoide transforma los valores numéricos en un rango entre 0 y 1,"""
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
