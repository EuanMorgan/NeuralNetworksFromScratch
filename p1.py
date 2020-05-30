#basic illustration of how a neuron in a neural network might work

inputs = [1.2,5.1,2.1] #unique inputs from (ficitonal) neurons in previous layer
weights = [3.1,2.1,8.7] #every neuron input is weighted
bias = 3 #every unique neuron has its own bias

output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias 
print(output)