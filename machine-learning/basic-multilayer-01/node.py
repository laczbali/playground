from enum import Enum
from typing import List
import numpy
from connection import Connection

class NodeType(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3

class NodeState(Enum):
    INACTIVE = 1
    ACTIVE = 2

class Node:

    # A node is in INACTIVE state by default
    # Once it starts to receive inputs, from connections behind it, it becomes ACTIVE

    def __init__(self, id, type: NodeType):
        self.id = id
        self.connections: List[Connection] = []
        self.type = type

        self.input_count = 0
        self.inputs_received = 0
        self.input_sum = 0
        self.state = NodeState.INACTIVE

    def feed_forward(self):
        output = self.activation_f()
        for connection in self.connections:
            connection.feed_forward(output)

        self.state = NodeState.INACTIVE
        self.inputs_received = 0

    def receive_input(self, input_value):
        if self.state == NodeState.INACTIVE:
            self.state = NodeState.ACTIVE
            self.input_sum = 0
            
        self.input_sum += input_value

        self.inputs_received += 1
        if self.inputs_received >= self.input_count:
            self.feed_forward()

    def activation_f(self):
        return numpy.tanh(self.input_sum)

    def get_output(self):
        return self.activation_f()

