import numpy as np

class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()

    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return 1 if weighted_sum >= 0 else 0

    def train(self, inputs, target, learning_rate=0.1, epochs=100):
        for epoch in range(epochs):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i])
                error = target[i] - prediction
                self.weights += learning_rate * error * inputs[i]
                self.bias += learning_rate * error

and_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
and_targets = np.array([0, 0, 0, 1])

and_perceptron = Perceptron(input_size=2)

and_perceptron.train(and_inputs, and_targets)

test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print("Input\t\tOutput")
for test_input in test_inputs:
    prediction = and_perceptron.predict(test_input)
    print(f"{test_input}\t\t{prediction}")
