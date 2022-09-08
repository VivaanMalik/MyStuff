import numpy as np

class ActivationFunctionCode():
    def __init__(self):
        self.NoFunction = 0
        self.StepFunction = 1
        self.SigmoidFunction = 2
        self.ReLUFunction = 3
        self.SiLUFunction = 4
        self.HyperbolicTangentFunction = 5

class Network(): # Just 2 layers for now
    def __init__(self, inputnum, outputnum, ACode):
        self.weights = np.random.rand(inputnum, outputnum)
        self.biases = np.random.rand(outputnum)
        self.ACode = ACode
        self.NodeValues = np.zeros(outputnum)

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
    
    def CalculateNodeValues(self, inputs):
        self.NodeValues = self.ActivationFunction(np.dot(inputs.astype(float), self.weights)+self.biases) # Calculate A(wx)
        return self.NodeValues

    def GradientDescent(self, error, inputs, outputs, lr):
        WeightAdjustments = np.dot(inputs.T, (lr*error*self.ActivationFunctionDerivative(outputs)))
        self.weights+=WeightAdjustments

        BiasAdjustments = np.average(lr*error)
        self.biases+=BiasAdjustments

    def Train(self, inputs, outputs, iterations, Learnrate):
        for _i in range(iterations):
            self.CalculateNodeValues(inputs)
            Errors = outputs - self.NodeValues
            self.GradientDescent(Errors, inputs, outputs, Learnrate)

TrainingInput=np.array([[0, 0, 1, 1],
                       [1, 1, 0, 1],
                       [1, 0, 1, 0],
                       [0, 1, 1, 1], 
                       [0, 0, 0, 0]])    
TrainingOutput=np.array([[0, 1, 1, 0, 0]]).T # Transpose

iter = int(input("Iterations: "))
lr = float(input("Learn rate: "))

N = Network(4, 1, ActivationFunctionCode().SigmoidFunction)
N.Train(TrainingInput, TrainingOutput, iter, lr)

while True:
    I1 = str(input("Input 1: "))
    I2 = str(input("Input 2: "))
    I3 = str(input("Input 3: "))
    I4 = str(input("Input 3: "))
    N.CalculateNodeValues(np.array([I1, I2, I3, I4]))
    print(N.NodeValues)
    if input("> ")=="exit":
        break
