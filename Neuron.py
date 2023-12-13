from math import exp

class Neuron():
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.size = len(weights)

    def summation(self, previousLayer):
        result = self.bias
        for neuron in previousLayer:
            for weight in self.weights:
                result += neuron.output * weight
        return result

    def activation(self, previousLayer):
        self.output = 1 / (1 + exp(-self.summation(previousLayer)))