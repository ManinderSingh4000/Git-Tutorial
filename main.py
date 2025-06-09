import numpy as np
def generate_random_array(size):
    return np.random.rand(size)

def calculate_mean(array):
    return np.mean(array)   

print(calculate_mean(generate_random_array(10)))