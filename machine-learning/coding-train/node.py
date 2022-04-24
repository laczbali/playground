import random
from typing import List


class Node:

    def __init__(self, inputcount, learning_rate=0.1):
        self.weights = []
        self.learning_rate = learning_rate # can be thought of as "steering intensity"

        # add a random weight for each input, plus one for the bias
        # the bias is needed, because a (0,0) input would always return 0 otherwise
        #     0 * any_weight = 0
        for i in range(inputcount + 1):
            self.weights.append(
                random.uniform(-1, 1)
            )

    def guess(self, inputs: List[float]):
        # add the bias to the inputs
        inputs.append(1)

        # sum the inputs (x1 * w1 + x2 * w2 + ... + xn * wn)
        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]

        # return the activation of the sum
        return self.activation(sum)

    def activation(self, sum):
        return 1 if sum >= 0 else -1

    def train(self, inputs: List[float], target: int):
        # take a guess
        guess = self.guess(inputs)
        error = target - guess

        # adjust weights based on the errors
        for i in range(len(inputs)):
            self.weights[i] += inputs[i] * error * self.learning_rate