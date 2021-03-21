import numpy as np
np.random.seed(69420)

X = [[1.2,7,2.5],
        [1.8,5,2.1],
        [1,2,1.9]]


class Layer_Dense:
        def __init__(self, n_inputs, n_neurons) -> "Layer":
                self.weights = np.random.randn(n_inputs, n_neurons) * 0.1
                self.biases =  np.zeros((1, n_neurons))
        def forward(self, inputs):
                self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(3,5)
layer2 = Layer_Dense(5,5)
layer3 = Layer_Dense(5,2)

layer1.forward(X)
layer2.forward(layer1.output)
layer3.forward(layer2.output)

print(layer3.output)