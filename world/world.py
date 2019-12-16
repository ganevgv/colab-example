import numpy as np


class World:
    def __init__(self, name):
        self.name = name

    def greet(self):
        txt = f"Hello, {self.name}! Your random number is {np.random.random():.4f}"
        print(txt)
