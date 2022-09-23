import numpy as np

def rosenbrock(x : list, 
            a : float = 1, 
            b : float = 100):
    """
    The multivariate Rosenbrock function
    """
    x = np.array(x)
    return np.sum(b * (x[1:] - x[:-1]**2)**2 + (a-x[:-1])**2)


    