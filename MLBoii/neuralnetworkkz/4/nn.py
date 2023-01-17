import numpy as np

np.set_printoptions(suppress=True)

class NeuralNetwork:
    def __init__(self, layers, activations):
        self.layers = layers
        self.values=[0]*len(layers)
        self.derivatives=[0]*(len(layers)-1)
        self.activations = activations
        self.weights = []
        self.biases = []
        for i in range(len(layers)-1):
            w = np.random.randn(layers[i], layers[i+1])
            b = np.random.randn(layers[i+1])
            self.weights.append(w)
            self.biases.append(b)
    
    def forward(self, x):
        self.values[0] =x
        for i, (w, b, activation) in enumerate(zip(self.weights, self.biases, self.activations)):
            x = self.activate(np.dot(x, w) + b, activation)
            self.values[i+1]=x
        return x
    
    def activate(self, x, activation):
        x.astype("float64")
        if activation == "sigmoid":
            return 1 / (1 + np.exp(-x))
        elif activation == "relu":
            return np.maximum(0, x)
        elif activation == "tanh":
            return np.tanh(x)
        else:
            raise ValueError(f"Invalid activation function: {activation}")

    def activate_derivative(self, x, activation):
        if activation == "sigmoid":
            return 1 / (1 + np.exp(-x)) * (1 - (1 / (1 + np.exp(-x))))
        elif activation == "relu":
            for i in range(0, len(x)):
                if isinstance(x[i], int):
                    x[i]=0 if x[i] < 0 else 1
                else:
                    for j in range(0, len(x[i])):
                        x[i][j]=0 if x[i][j] < 0 else 1
            return x
        elif activation == "tanh":
            return 1-((np.exp(2*x)-1)/(np.exp(2*x)+1))**2
        else:
            raise ValueError(f"Invalid activation function: {activation}")
    
    def backward(self, y, learning_rate, output):
        grad_weights = [np.zeros(w.shape) for w in self.weights]
        grad_biases = [np.zeros(b.shape) for b in self.biases]

        error = y - output


        for i in reversed(range(len(self.layers)-1)):
            error = error * self.activate_derivative(self.values[i+1], self.activations[i])

            error_re = error.reshape(error.shape[0], -1).T
            current_activations = self.values[i]
            current_activations=current_activations.reshape(current_activations.shape[0],-1)

            self.derivatives[i] = np.dot(error_re, current_activations)

            # grad_weights2=[]
            # for j in range(len(error_re)):
            #     grad_weights2.append(np.dot(np.array([current_activations[j]]), np.array([error_re[j]])))
            # grad_weights[i]=np.array(grad_weights2)

            # self.derivatives[i]=grad_weights[i]

            error2 = []
            for j in error:
                error2.append(np.dot(np.array([j]), self.weights[i].T))
            error=np.array(error2[0])
        
        self.gradient_descent()

    def gradient_descent(self):
        for i in range(len(self.derivatives)):
            for j in self.derivatives[i]:
                print(self.derivatives[i])
                print(self.weights[i])
                self.weights[i] -= learning_rate * j
    


nn = NeuralNetwork([4, 3, 1], ["relu", "sigmoid"])

# Train the network using gradient descent
num_epochs=int(input("Number of epochs:\n"))
learning_rate=0.1

x_train = np.array([[1, 0, 0, 1], [0, 1, 0, 0], [0, 1, 1, 1], [1, 0, 1, 0], [0, 0, 0, 1], [1, 0, 1, 1], [0, 1, 1, 0]], dtype=float)
y_train = np.array([[1, 0], [0, 1], [0, 1], [1, 0], [0, 1], [1, 0], [0, 1]], dtype=float)
y_train2 = np.array([[1], [0], [0], [1], [0], [1], [0]], dtype=float)

for i in range(num_epochs):
    output = nn.forward(x_train)
    nn.backward(y_train2, learning_rate, output)

# TEst
print(nn.forward(x_train)-y_train)
while True:
    i1=float(input("Input number 1: \n"))
    i2=float(input("Input number 2: \n"))
    i3=float(input("Input number 3: \n"))
    i4=float(input("Input number 4: \n"))
    print(nn.forward([[i1, i2, i3, i4]]))