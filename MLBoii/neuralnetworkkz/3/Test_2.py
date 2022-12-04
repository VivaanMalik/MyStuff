from matplotlib.pyplot import axis
import numpy as np
import json

np.set_printoptions(suppress=True)

class ActivationFunctionCode():
    def __init__(self):
        self.NoFunction = 0
        self.StepFunction = 1
        self.SigmoidFunction = 2
        self.ReLUFunction = 3
        self.SiLUFunction = 4
        self.HyperbolicTangentFunction = 5

class Layer():
    def __init__(self, layerNodes, weights, biases):
        self.NodeValues = np.zeros(layerNodes)
        self.weights = weights
        self.biases = biases

class Network(): # Just 2 layers for now
    def __init__(self, layers, ACode, MakeNewWeightsBiases, filename):
        self.Layers=[]
        if MakeNewWeightsBiases:
            for l in range(len(layers)-1):
                weights=np.random.rand(layers[l], layers[l+1])
                biases=np.random.rand(layers[l+1])
                self.Layers.append(Layer(layers[l+1], weights, biases))
        else:
            data = json.load(open(filename, encoding='utf-8'))
            for l in range(1, len(layers)):
                weights = np.array(data[len(data)-1]["Weights"][l-1])
                biases = np.array(data[len(data)-1]["Biases"][l-1])
                self.Layers.append(Layer(layers[l], weights, biases))
        self.name = filename
        self.ACode = ACode

    def ActivationFunction(self, x):
        if self.ACode == ActivationFunctionCode().NoFunction:
            return x
        elif self.ACode == ActivationFunctionCode().StepFunction:
            return 1 if x > 0 else 0
        elif self.ACode == ActivationFunctionCode().SigmoidFunction:
            return 1/(1+np.exp(-x))
        elif self.ACode == ActivationFunctionCode().ReLUFunction:
            return np.maximum(0, x)
        elif self.ACode == ActivationFunctionCode().SiLUFunction:
            return x/(1+np.exp(-x))
        elif self.ACode == ActivationFunctionCode().HyperbolicTangentFunction:
            return (np.logaddexp(x, x)-1)/(np.logaddexp(x, x)+1)
        else:
            return x

    def ActivationFunctionDerivative(self, x):
        if self.ACode == ActivationFunctionCode().NoFunction:
            return 1
        elif self.ACode == ActivationFunctionCode().StepFunction:
            return 1
        elif self.ACode == ActivationFunctionCode().SigmoidFunction:
            return (1/(1+np.exp(-x)))*(1-(1/(1+np.exp(-x))))
        elif self.ACode == ActivationFunctionCode().ReLUFunction:
            return 0 if x<0 else 1
        elif self.ACode == ActivationFunctionCode().SiLUFunction:
            return (1/(1+np.exp(-x)))*(1+(x*(1-(1/(1+np.exp(-x))))))
        elif self.ACode == ActivationFunctionCode().HyperbolicTangentFunction:
            return 1-((np.exp(2*x)-1)/(np.exp(2*x)+1))**2
        else:
            return 1
    
    def CalculateNodeValues(self, input):
        PreviousInput=input.astype(float)
        for l in range(len(self.Layers)):
            self.Layers[l]:Layer
            self.Layers[l].NodeValues=self.ActivationFunction(np.dot(PreviousInput, self.Layers[l].weights)+self.Layers[l].biases)
            PreviousInput=self.Layers[l].NodeValues

    def BackPropogationGradientDescent(self, error, input, ExpectedOutputs, LearnRate):
        
        W_Gradient_Adjust = -error*self.ActivationFunctionDerivative(ExpectedOutputs-error)
        B_Gradient_Adjust = -error*self.ActivationFunctionDerivative(ExpectedOutputs-error)

        for l in range(len(self.Layers)-1, 0, -1):
            for w in range(W_Gradient_Adjust.size):
                self.Layers[l-1].weights+=np.tile((W_Gradient_Adjust[w]*self.Layers[l-1].NodeValues), (len(self.Layers[l].NodeValues), 1))

            # W_Gradient_Adjust*=np.average(self.ActivationFunctionDerivative(self.Layers[l-1].NodeValues), axis=0)
            # W_Gradient_Adjust=np.average(self.Layers[l-1].NodeValues.T, axis=1)[:, None]*W_Gradient_Adjust.T*LearnRate

            # B_Gradient_Adjust=self.Layers[l-1].weights[:, None] * np.average(B_Gradient_Adjust.T)
            # B_Gradient_Adjust*=np.average(self.ActivationFunctionDerivative(self.Layers[l-1].NodeValues), axis=0)
            # B_Gradient_Adjust=np.average(B_Gradient_Adjust.T*LearnRate)


        W_Gradient_Adjust=W_Gradient_Adjust * np.average(input)
        self.Layers[0].weights+=W_Gradient_Adjust.T
        self.Layers[0].biases+=B_Gradient_Adjust.T

    def Train(self, inputs, ExpectedOutputs, iterations, Learnrate):
        for _i in range(iterations):
            self.CalculateNodeValues(inputs)
            Errors = ExpectedOutputs - self.Layers[len(self.Layers)-1].NodeValues
            self.BackPropogationGradientDescent(Errors, inputs, ExpectedOutputs, Learnrate)

    def SaveData(self):
        data:list = json.load(open(self.name, encoding='utf-8'))
        Weights = []
        Biases = []
        for l in self.Layers:
            l:Layer
            Weights.append(l.weights.tolist())
            Biases.append(l.biases.tolist())
        data.append({"Weights":Weights, "Biases":Biases})
        with open(self.name, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=False)

TrainingInput=np.array([[0, 0, 1, 1],
                       [1, 1, 0, 1],
                       [1, 0, 1, 0],
                       [0, 1, 1, 1],
                       [0, 0, 1, 0]])    
TrainingOutput=np.array([[0, 1, 1, 0, 0]]).T # Transpose

iter = int(input("Iterations: "))
lr = float(input("Learn rate: "))

N = Network([4, 2, 1], ActivationFunctionCode().SigmoidFunction, True, "WeightsBiasesData.json")
N.Train(TrainingInput, TrainingOutput, iter, lr)

while True:
    I1 = str(input("Input 1: "))
    I2 = str(input("Input 2: "))
    I3 = str(input("Input 3: "))
    I4 = str(input("Input 4: "))
    N.CalculateNodeValues(np.array([[I1, I2, I3, I4]]))
    print("\nWeights And Biases (per layer):\n")
    for l in N.Layers:
        print(l.weights)
        print(l.biases)
        print("\n")
    print("Output: ", N.Layers[len(N.Layers)-1].NodeValues)
    x=input("> ")
    if x=="exit":
        break
    elif x == "add":
        N.SaveData()