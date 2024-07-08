import numpy as np

class Ben:
    def __init__(self):
        self.name = 'Ben'

    def say_hello(self):
        return f'Hello, my name is {self.name}'
    
    def print_vector(self):
        import numpy as np

        matrix = np.zeros([3, 3])
        print("\nMatrix : \n", matrix)
    

class Tom:
    def __init__(self):
        self.name = 'Tom'

    def say_hello(self):
        return f'Hello, my name is {self.name}'