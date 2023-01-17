from random import random
import numpy as np

class Perceptron():
    def __init__(self, Layers):
        self.LayerCount = len(Layers)

        self.SynapticWeights = []
        self.SynapticWeightDerivatives = []
        self.LayerNodeValues = []

        for i in range(len(Layers)-1):
            self.SynapticWeights.append(np.random.rand(Layers[i], Layers[i+1]))
            self.SynapticWeightDerivatives.append(np.zeros((Layers[i], Layers[i+1])))

        for i in range(len(Layers)):
            self.LayerNodeValues.append(np.zeros(Layers[i]))
    
    def activation(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def activation_derivative(self, x):
        return x * (1.0 - x)
        
    def forward(self, inputs):
        value = inputs
        self.LayerNodeValues[0]=value
        for i in range(self.LayerCount-1):
            value=self.activation(np.dot(value, self.SynapticWeights[i]))
            self.LayerNodeValues[i+1]=value
        return value
    
    def backwards(self, error):
        for i in reversed(range(self.LayerCount-1)):
            derivative = error*self.activation_derivative(self.LayerNodeValues[i+1])
            derivative2d = derivative.reshape(derivative.shape[0], -1)
            NodeValues=self.LayerNodeValues[i]
            NodeValues=NodeValues.reshape(NodeValues.shape[0], -1).T
            self.SynapticWeightDerivatives[i] = np.dot(NodeValues, derivative2d)
            error = np.dot(derivative, self.SynapticWeights[i].T)

    def descent(self, lr):
        for i in range(self.LayerCount-1):
            self.SynapticWeights[i] += self.SynapticWeightDerivatives[i] * lr
    
    def train(self, Input, ExpectedOutput, Epochs, LearningRate):
        for i in range(Epochs):
            ActualOuput = self.forward(Input)
            error = ExpectedOutput - ActualOuput
            self.backwards(error)
            self.descent(LearningRate)

x_train = np.array([[1, 0, 0, 1], [0, 1, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 1], [1, 0, 1, 1], [0, 1, 1, 0]], dtype=float)
y_train2 = np.array([[1], [0], [0], [1], [0], [1], [0]], dtype=float)

p = Perceptron([4, 3, 1])
epochs = int(input("Epochs:\n"))
lr = float(input("Learn rate:\n"))
p.train(x_train, y_train2, epochs, lr)

while True:
    i1 = float(input("Number 1:\n"))
    i2 = float(input("Number 2:\n"))
    i3 = float(input("Number 3:\n"))
    i4 = float(input("Number 4:\n"))
    print(p.forward(np.array([i1, i2, i3, i4])))