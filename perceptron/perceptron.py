import numpy as np


class Perceptron:
    def __init__(self):
        self.weightA = np.random.rand()
        self.weightB = np.random.rand()
        self.bias = np.random.rand()

    def predict(self, weightA, weightB):
        sum = self.weightA * weightA + self.weightB * weightB + self.bias

        return np.sign(sum)

    def train(self, weightA, weightB, expected_output):
        actual_output = self.predict(weightA, weightB)

        error = expected_output - actual_output

        self.weightA += weightA * error
        self.weightB += weightB * error
        self.bias += error


perceptron = Perceptron()

x1 = [1, 2, 3, 4, 5]
x2 = [1, 2, 3, 4, 5]
expected_output = [1, 2, 3, 4, 5]

for i in range(len(x1)):
    perceptron.train(x1[i], x2[i], expected_output[i])


print(perceptron.predict(1, 2))
print(perceptron.predict(4, 5))
