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

class Network(): # Just 2 layers for now
    def __init__(self, layers, ACode, MakeNewWeightsBiases, filename):
        if MakeNewWeightsBiases:
            self.weights=[]
            self.biases=[]
            for l in range(len(layers)-1):
                self.weights.append(np.random.rand(layers[l], layers[l+1]))
                self.biases.append(np.random.rand(layers[l+1]))
        else:
            data = json.load(open(filename, encoding='utf-8'))
            self.weights = data[len(data)-1]["Weights"]
            self.biases = data[len(data)-1]["Biases"]
        self.name = filename
        self.ACode = ACode
        self.NodeValues=[]
        for l in range(len(layers)-1):
            self.NodeValues.append(np.zeros(layers[l+1]))
    
    def OptimizeX(self, x):
        for e1 in range(len(x)):
            for e2 in range(len(x[e1])):
                x[e1][e2] = min(300, x[e1][e2])

    def ActivationFunction(self, x):
        self.OptimizeX(x)
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
    
    def CalculateNodeValues(self, inputs):
        PreviousLayerOutput=inputs.astype(float)

        for l in range(len(self.NodeValues)):
            self.NodeValues[l] = self.ActivationFunction(np.dot(PreviousLayerOutput, self.weights[l])+self.biases[l]) # Calculate A(wx)
            # print(np.dot(PreviousLayerOutput, self.weights[l])+self.biases[l])
            PreviousLayerOutput = self.NodeValues[l]
        return self.NodeValues

    def GradientDescent(self, error, inputs, outputs, lr):
        WeightAdjustments=error
        BiasAdjustments = error

        for l in range(len(self.NodeValues)-1, 0, -1):
            AddedWeights = self.weights[l][0]
            for w in range(1, self.weights[l].size):
                AddedWeights+=self.weights[l][w]

            WeightAdjustments*=AddedWeights *self.ActivationFunctionDerivative(self.NodeValues[l])           
            self.weights[l]+=lr*np.dot(self.NodeValues[l-1].T, WeightAdjustments)

            BiasAdjustments*=self.ActivationFunctionDerivative(self.NodeValues[l])
            self.biases[l]+=lr*np.average(BiasAdjustments)

        # print(self.NodeValues[0])
        WeightAdjustments=self.ActivationFunctionDerivative(self.NodeValues[0])*WeightAdjustments
        self.weights[0]+= np.dot(inputs.T, lr*WeightAdjustments)
        # BiasAdjustments*=self.ActivationFunctionDerivative(self.NodeValues[0])
        self.biases[0]+= np.average(lr*BiasAdjustments)

    def Train(self, inputs, outputs, iterations, Learnrate):
        for _i in range(iterations):
            self.CalculateNodeValues(inputs)
            Errors = outputs - self.NodeValues[len(self.NodeValues)-1]
            self.GradientDescent(Errors, inputs, outputs, Learnrate)
    
    def SaveData(self):
        data = json.load(open(self.name, encoding='utf-8'))
        data.append({"Weights":self.weights.tolist(), "Biases":self.biases.tolist()})
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
    I4 = str(input("Input 3: "))
    N.CalculateNodeValues(np.array([[I1, I2, I3, I4]]))
    print(N.NodeValues[len(N.NodeValues)-1])
    x=input("> ")
    if x=="exit":
        break
    elif x == "add":
        N.SaveData()