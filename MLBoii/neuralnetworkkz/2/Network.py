import numpy as np

class ActivationFunctionCode():
    def __init__(self):
        self.NoFuntion = 0
        self.StepFuntion = 1
        self.SigmoidFuntion = 2
        self.ReLUFuntion = 3
        self.SiLUFuntion = 4
        self.HyperbolicTangentFuntion = 5

class Layer():
    
    def __init__(self, num_inputs, nodes, activation_funtion_code, LearnRate):
        self.NodeValues = np.zeros(nodes)
        self.Input = np.zeros(num_inputs)
        self.SynapticWeights = np.random.rand(nodes, num_inputs)
        self.WeightBiases = np.random.rand(nodes)
        self.ActivationFunctionCode = activation_funtion_code
        self.Error = np.zeros(nodes)
        self.CostGradientBiases = np.zeros(nodes)
        self.CostGradientWeights = np.zeros((nodes, num_inputs))
        self.LearnRate = LearnRate
        self.ExpectedOutput = np.zeros(nodes)
    
    def simplify_x(self, x):
        x=round(x, 1)
        x=min(x, 1000)
        return x
    
    def simplify_x_2(self, x):
        x=round(x, 4)
        x=min(x, 10)
        return x

    def ActivationFunction(self, x):
        x=self.simplify_x(x)
        if self.ActivationFunctionCode == ActivationFunctionCode().NoFuntion:
            return x
        elif self.ActivationFunctionCode == ActivationFunctionCode().StepFuntion:
            return  1 if x > 0 else 0
        elif self.ActivationFunctionCode == ActivationFunctionCode().SigmoidFuntion:
            return 0 if (1+np.exp(-x)) == 0 else 1/(1+np.exp(-x))
        elif self.ActivationFunctionCode == ActivationFunctionCode().ReLUFuntion:
            return np.maximum(0, x)
        elif self.ActivationFunctionCode == ActivationFunctionCode().SiLUFuntion:
            return 0 if (1+np.exp(-x))==0 else x/(1+np.exp(-x))
        elif self.ActivationFunctionCode == ActivationFunctionCode().HyperbolicTangentFuntion:
            return 0 if (np.logaddexp(x, x)+1) == 0 else (np.logaddexp(x, x)-1)/(np.logaddexp(x, x)+1)
        else:
            return x

    def ActivationFunctionDerivative(self, x):
        x=self.simplify_x_2(x)
        if self.ActivationFunctionCode == ActivationFunctionCode().NoFuntion:
            return 1
        elif self.ActivationFunctionCode == ActivationFunctionCode().StepFuntion:
            return  float("inf") if x == 0 else 0
        elif self.ActivationFunctionCode == ActivationFunctionCode().SigmoidFuntion:
            return 0 if (1+np.exp(-x)) == 0 else (1/(1+np.exp(-x)))*(1-(1/(1+np.exp(-x))))
        elif self.ActivationFunctionCode == ActivationFunctionCode().ReLUFuntion:
            return 0 if x<0 else 1
        elif self.ActivationFunctionCode == ActivationFunctionCode().SiLUFuntion:
            return 0 if (1+np.exp(-x)) == 0 else (1/(1+np.exp(-x)))*(1+(x*(1-(1/(1+np.exp(-x))))))
        elif self.ActivationFunctionCode == ActivationFunctionCode().HyperbolicTangentFuntion:
            return 0 if (np.exp(2*x)+1) == 0 else 1-((np.exp(2*x)-1)/(np.exp(2*x)+1))**2
        else:
            return 1
    
    def CalculateGradient(self, EO, ActualOutput, MultipleInputIters, Inputs):
        FinalError=EO[0]-ActualOutput[0]
        FinalInputs = Inputs[0]
        for i in range(1, MultipleInputIters):
            FinalError += EO[i]-ActualOutput[i]
            FinalInputs+=Inputs[i]

        for n in range (self.NodeValues.size):
            #Caculate Derivative of dCost/dBias
            CostBiasDerivative = 2*FinalError/MultipleInputIters
            self.CostGradientBiases[n] = CostBiasDerivative
            for i in range (self.Input.size):
                # Calculate Derivative of dCost/dWeight
                CostWeightDerivative = FinalInputs[i] * FinalError * self.ActivationFunctionDerivative(self.NodeValues[n])/MultipleInputIters
                self.CostGradientWeights[n][i] = CostWeightDerivative

    def GradientDescent(self):
        for n in range(self.NodeValues.size):
            self.WeightBiases[n] += self.CostGradientBiases[n] * self.LearnRate
            for i in range(self.Input.size):
                self.SynapticWeights[n][i] -= self.CostGradientWeights[n][i] * self.LearnRate

    def CalculateNodeActivationValues(self, input):
        self.Input=input
        for n in range(self.NodeValues.size):
            self.NodeValues[n] = 0.0
            for i in range(len(input)):
                self.NodeValues[n] += input[i]*self.SynapticWeights[n][i]
            self.NodeValues[n] += self.WeightBiases[n]
            self.NodeValues[n] = self.ActivationFunction(self.NodeValues[n])
    
    def GetOutput(self):
        output_array = np.zeros(len(self.NodeValues))
        for n in range(self.NodeValues.size):
            output_array[n] = self.NodeValues[n]
        return output_array

    
    def GetError(self, ExpectedOutput):
        self.ExpectedOutput = ExpectedOutput
        for n in range(self.NodeValues.size):
            self.Error[n] = (ExpectedOutput-self.NodeValues[n])**2
        return self.Error

class NeuralNetwork():
    def __init__(self, Layers:Layer, Activation_Funtion_Code, LearnRate, Iterations):
        self.iters = Iterations
        self.AFC = Activation_Funtion_Code
        self.LR = LearnRate
        self.Layers = []
        for i in range(len(Layers)-1):
            self.Layers.append(Layer(Layers[i], Layers[i+1], Activation_Funtion_Code, LearnRate))
        
    def Train(self, input, expected_output, multiple_inputs):            
        for iter in range(self.iters):
            MultipleInputIters = 1
            if multiple_inputs:
                MultipleInputIters = len(input)
            
            Error = 0.0
            EOList = []
            OutputList = []
            Inputs = []
            for m in range(MultipleInputIters):
                if multiple_inputs:
                    EO = expected_output[m]
                    PreviousOutput = input[m]
                else:
                    EO = expected_output
                    PreviousOutput = input
                Inputs.append(PreviousOutput)
                for i in range(len(self.Layers)):
                    self.Layers[i].CalculateNodeActivationValues(PreviousOutput)
                    PreviousOutput=self.Layers[i].GetOutput()
                EOList.append(EO)
                OutputList.append(self.Layers[len(self.Layers)-1].GetOutput())
                Error += self.Layers[len(self.Layers)-1].GetError(EO)
            Error/=MultipleInputIters


            for i in range(len(self.Layers)):
                self.Layers[i].CalculateGradient(EOList, OutputList, MultipleInputIters, Inputs)

            if iter != self.iters-1:
                for i in range(len(self.Layers)-1, -1, -1):
                    self.Layers[i].GradientDescent()
    
    def Think(self, input):
        PreviousOutput = input
        for i in range(len(self.Layers)):
            self.Layers[i].CalculateNodeActivationValues(PreviousOutput)
            PreviousOutput=self.Layers[i].GetOutput()
        return PreviousOutput

# == Training Data ==
Inputs =   np.array([np.array([0, 0, 1]),
                    np.array([1, 1, 0]),
                    np.array([1, 0, 1]),
                    np.array([0, 1, 1]),
                    np.array([0, 0, 0])])
Inputs = Inputs.astype(float)

Expected_Output_Training = np.array([np.array([0]), np.array([1]), np.array([1]), np.array([0]), np.array([0])])
Expected_Output_Training = Expected_Output_Training.astype(float)

iterations = int(input("Iterations:\n"))
LearnRate = float(input("Learn Rate:"))

NN = NeuralNetwork([3, 1], ActivationFunctionCode().SigmoidFuntion, LearnRate, iterations)
NN.Train(Inputs, Expected_Output_Training, True)

# == Test == ....checks if 1st digit is 1 or 0
Test = True
while Test:
    Input_1_Test = float(input("==Test==\nInput 1:\n"))
    Input_2_Test = float(input("Input 2:\n"))
    Input_3_Test = float(input("Input 3:\n"))
    # Input_4_Test = float(input("Input 4:\n"))

    Answer = NN.Think([Input_1_Test, Input_2_Test, Input_3_Test])
    for i in range(Answer.size):
        Answer[i]=round(Answer[i], 6)
    print(Answer)
    Test=False if input("Exit? (Type 'Y' to exit)\n") == "Y" else True