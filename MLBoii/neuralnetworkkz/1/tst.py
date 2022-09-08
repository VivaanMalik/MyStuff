import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoide_dervativ(x):
    return x*(1-x)

train_inputz=np.array([[0, 0, 1],
                       [1, 1, 1],
                       [1, 0, 1],
                       [0, 1, 1]])
train_outputz=np.array([[0, 1, 1, 0]]).T

np.random.seed(1)
synaptic_weights=2*np.random.random((3, 1))-1

print('rendum starting synaptic weights:\n {}\n'.format(synaptic_weights))
for i in range(500000):
    #error=output-actual output
    #input=0 or 1
    #weight adjustion=error*input*[weird symbol]'(output)
    input_layer=train_inputz
    outputs=sigmoid(np.dot(input_layer, synaptic_weights)) # normalises the matrix product of the input and weights
    error=train_outputz-outputs

    adjust=error*sigmoide_dervativ(outputs)
    synaptic_weights+=np.dot(input_layer.T, adjust)

print("Synaptic weights afta trening:\n {}\n".format(synaptic_weights))

print("Output afta trening:\n {}\n".format(outputs))