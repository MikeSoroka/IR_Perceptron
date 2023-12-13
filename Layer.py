from Neuron import Neuron

class Layer():
    def __init__(self, weights, biases):
        self.data = []
        currentNeuron = 0
        for single_neuron_weights in weights:
            neuron = Neuron(single_neuron_weights, biases[currentNeuron])
            self.data.append(neuron)
            currentNeuron == 1
        self.size = currentNeuron + 1

    def activate(self, previousLayer):
        for neuron in self.data:
            neuron.activation(previousLayer)

    def Get(self, i):
        return self.data[i]

