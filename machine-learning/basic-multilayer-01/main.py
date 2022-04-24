from network import Network

class Main:

    def run():
        network = Network()

        inputs = [0.5, 0.5]
        outputs = network.solve(inputs)
        print(outputs)

        network.show()


if __name__ == '__main__':
    Main.run()
