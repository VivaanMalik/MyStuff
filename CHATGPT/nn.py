import numpy as np

np.set_printoptions(suppress=True)

class NeuralNetwork:
    def __init__(self, layers, activations):
        self.layers = layers
        self.activations = activations
        self.weights = []
        self.biases = []
        for i in range(len(layers)-1):
            w = np.random.randn(layers[i], layers[i+1])
            b = np.random.randn(layers[i+1])
            self.weights.append(w)
            self.biases.append(b)
    
    def forward(self, x):
        for w, b, activation in zip(self.weights, self.biases, self.activations):
            x = self.activate(np.dot(x, w) + b, activation)
        return x
    
    def activate(self, x, activation):
        if activation == "sigmoid":
            return 1 / (1 + np.exp(-x))
        elif activation == "relu":
            return np.maximum(0, x)
        elif activation == "tanh":
            return np.tanh(x)
        else:
            raise ValueError(f"Invalid activation function: {activation}")
    
    def backward(self, x, y, learning_rate, output):
        grad_weights = [np.zeros(w.shape) for w in self.weights]
        grad_biases = [np.zeros(b.shape) for b in self.biases]

        error = y - output


        for i in reversed(range(len(self.layers)-1)):
            print(i)
            print("error:")
            print(error)
            error = error * self.activate(output, self.activations[i])
            print("error:")
            print(error)
            print("weights:")
            print(self.weights[i].T)

            grad_weights[i] = np.dot(x.T, error)
            grad_biases[i] = np.sum(error, axis=0)
            error = np.dot(error, self.weights[i].T)
        self.weights = [w + learning_rate * gw for w, gw in zip(self.weights, grad_weights)]
        self.biases = [b + learning_rate * gb for b, gb in zip(self.biases, grad_biases)]

nn = NeuralNetwork([4, 3, 2], ["sigmoid", "relu"])

# Train the network using gradient descent
num_epochs=5000
learning_rate=0.3

x_train = np.array([[1, 0, 0, 1], [0, 1, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0]])
y_train = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])

for i in range(num_epochs):
    output = nn.forward(x_train)
    nn.backward(x_train, y_train, learning_rate, output)

# TEst
i1=int(input("Input number 1: \n"))
i2=int(input("Input number 2: \n"))
i3=int(input("Input number 3: \n"))
i4=int(input("Input number 4: \n"))
print(nn.forward([[i1, i2, i3, i4]]))