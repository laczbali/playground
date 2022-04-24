import networkx as nx
import matplotlib.pyplot as plt

from node import Node, NodeType
from connection import Connection


class Network:

    def __init__(self):

        # obviously, this should not be configured like this in a real environment

        i1 = Node(0, NodeType.INPUT)
        i2 = Node(1, NodeType.INPUT)

        h1 = Node(2, NodeType.HIDDEN)
        h2 = Node(3, NodeType.HIDDEN)
        h3 = Node(4, NodeType.HIDDEN)
        
        o1 = Node(5, NodeType.OUTPUT)

        c1 = Connection(output_node=h1)
        c2 = Connection(output_node=h2)
        c3 = Connection(output_node=h3)
        
        i1.connections.extend([c1, c2])
        i2.connections.extend([c3])

        c4 = Connection(output_node=o1)
        c5 = Connection(output_node=o1)
        c6 = Connection(output_node=o1)

        h1.connections.extend([c4])
        h2.connections.extend([c5])
        h3.connections.extend([c6])

        self.input_nodes = [i1, i2]
        self.hidden_nodes = [h1, h2, h3]
        self.output_nodes = [o1]
        self.connections = [c1, c2, c3, c4, c5, c6]

    def solve(self, inputs = []):
        for i in range(len(inputs)):
            self.input_nodes[i].receive_input(inputs[i])

        outputs = []
        for node in self.output_nodes:
            outputs.append(node.get_output())

        return outputs

    def train(self, inputs = [], target_outputs = []):
        pass

    def show(self):
        all_nodes = self.input_nodes + self.hidden_nodes + self.output_nodes
        
        G = nx.Graph()
        for node in all_nodes:
            G.add_node(node.id)

        for node in all_nodes:
            for connection in node.connections:
                G.add_edge(node.id, connection.output_node.id)

        nx.draw(G, with_labels=True, pos=nx.spring_layout(G))
        plt.savefig("path.png")