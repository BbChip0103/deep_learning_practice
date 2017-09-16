import numpy as np

def step_function(x) :
    return np.array(x > 0, dtype = np.int)

def sigmoid(x) :
    return 1 / (1 + np.exp(-x))

def ReLU(x) :
    return np.maximum(0, x)

def identity_function(x) :
    return x

def softmax(a) :
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y
