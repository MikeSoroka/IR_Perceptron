from Layer import Layer

class NeuralNetwork():
    def __init__(self, weights_matrix, biases, chars_list, learning_rate):
        self.input = input
        self.learning_rate = learning_rate
        self.size = learning_rate.size
        self.chars_list = chars_list
        self.epochs = 0
        self.weights_matrix = weights_matrix
        self.biases = biases


    def activate(self, input):
        self.outputLayer = Layer(self.weights_matrix, self.biases)
        self.outputLayer.activate(input)

    def calculate_output(self):
        self.output = []
        for neuron in self.outputLayer:
            self.output.append(neuron.output)

    def MSE(self, expected_results):
        self.calculate_output()
        self.mistake = 0
        for i in range(self.size):
            self.mistake += (self.output[i] - expected_results[i])

    def epoch(self, input, expected_results):
        self.MSE(expected_results)
        self.epochs += 1
        self.activate(input)
        for i in range(self.size):
            neuron = Layer.Get(i)
            current_weight  = 0
            for weight in neuron.weights:
                weight += self.learning_rate * self.mistake *  input[current_weight]
                current_weight += 1
