import numpy as np
import matplotlib.pylab as plt
import function as fun

if __name__ == '__main__' :
    x = np.arange(-5.0, 5.0, 0.1)
    #y = fun.step_function(x)
    #y = fun.sigmoid(x)
    y = fun.ReLU(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 5)
    plt.show()
