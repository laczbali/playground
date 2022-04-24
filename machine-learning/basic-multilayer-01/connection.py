import random

class Connection:

    def __init__(self, weight=None, output_node=None):
        if weight is None:
            self.weight = random.uniform(-1, 1)
        else:
            self.weight = float(weight)
        self.output_node = output_node

    def feed_forward(self, input_value):
        self.output_node.receive_input(self.weight * input_value)
        