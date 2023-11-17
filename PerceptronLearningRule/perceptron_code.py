import numpy as np

# En esta calse implementamos la regla de aprendizaje del perceptron
class Perceptron:
    def __init__(self, no_of_inputs, threshold=100, learning_rate=0.01):
        # Inicializamos los parametros
        self.threshold = threshold
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_of_inputs + 1)
           
    def predict(self, inputs):
        # Funcion de activacion
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        # Funcion escalon
        if summation > 0:
            # Si la suma es mayor a 0, la salida es 1
          activation = 1
        else:
            # Si la suma es menor a 0, la salida es 0
          activation = 0            
        return activation

    def train(self, training_inputs, labels):
        # Entrenamiento del perceptron
        for _ in range(self.threshold):
            # Iteramos sobre los datos de entrenamiento
            for inputs, label in zip(training_inputs, labels):
                # Prediccion del perceptron
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)

# Funcion para leer los datos de entrenamiento desde un archivo
def read_training_data(filename):
  # Leemos kos datos
    data = np.loadtxt(filename, delimiter=',')
    # Separar las entradas de las salidas esperadas
    X = data[:, :-1] # Entradas esperadas
    y = data[:, -1] # Salidas esperadas
    return X, y

# Archivos conn los datos para el entrenamento
X, y = read_training_data('https://raw.githubusercontent.com/PaulQuezada/InteligenciaArtificial/main/Perceptron%20Learning%20Rule/perceptron_training_data.csv')

# Crear un perceptron con 2 entradas (ya que tenemos solo 2 caracteristicas en nuestro excel con los datos inventados)
perceptron = Perceptron(no_of_inputs=2)

# Entrenamos el perceptron 
perceptron.train(X, y)

# Imprimimos los pesos del perceptron
bias_weight = perceptron.weights[0]
input1_weight = perceptron.weights[1]
input2_weight = perceptron.weights[2]

weights_dict = {
    "Bias - Weight": bias_weight,
    "Weight para la entrada 1": input1_weight,
    "Weight para la entradat 2": input2_weight
}

weights_dict