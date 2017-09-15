import numpy as np

def AndGate(_x1, _x2) :
    x = np.array([_x1, _x2])
    w = np.array([0.5, 0.5])
    b = -0.9
    return (0 if (np.sum(w*x)+b <= 0) else 1)

def NandGate(_x1, _x2) :
    x = np.array([_x1, _x2])
    w = np.array([0.5, 0.5])
    b = -0.9
    return (1 if (np.sum(w*x)+b <= 0) else 0)

def OrGate(_x1, _x2) :
    x = np.array([_x1, _x2])
    w = np.array([0.5, 0.5])
    b = -0.4
    return (0 if (np.sum(w*x)+b <= 0) else 1)

def NorGate(_x1, _x2) :
    x = np.array([_x1, _x2])
    w = np.array([0.5, 0.5])
    b = -0.4
    return (1 if (np.sum(w*x)+b <= 0) else 0)

def XorGate(_x1, _x2) :
    s1 = NandGate(_x1, _x2)
    s2 = OrGate(_x1, _x2)
    y = AndGate(s1, s2)
    return y
