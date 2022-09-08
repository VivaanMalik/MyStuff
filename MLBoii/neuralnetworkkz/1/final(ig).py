#sheesh
import numpy as np

class NeuralNetwork():
    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights=2*np.random.random((4, 1))-1

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1-x)
    
    def train(self, inputs, outputs, iterations):
        for i in range(iterations):
            output=self.think(inputs)
            error=outputs-output
            adjustments = np.dot(inputs.T, error * self.sigmoid_derivative(output))
            #self.synaptic_weights = self.synaptic_weights + adjustments
            self.synaptic_weights+=adjustments
    
    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__=="__main__":
    
    iters=int(input("Learning iterations:"))
    neural_network=NeuralNetwork()

    train_inputz=np.array([[0, 0, 1, 1],
                           [1, 1, 0, 1],
                           [1, 0, 1, 0],
                           [0, 1, 1, 1]])

    train_outputz=np.array([[0, 1, 1, 0]]).T

    print("rendum synaptic weights:\n{}\n".format(neural_network.synaptic_weights))
    neural_network.train(train_inputz, train_outputz, iters)
    print("synaptic weights afta trening:\n{}\n".format(neural_network.synaptic_weights))
    
    print("\n===New situation===\n")
    A = str(input("Input 1: "))
    B = str(input("Input 2: "))
    C = str(input("Input 3: "))
    D = str(input("Input 3: "))

    
    print("New situation: input data = ", A, B, C, D)
    print("Output data: ")
    print(neural_network.think(np.array([A, B, C, D])))
