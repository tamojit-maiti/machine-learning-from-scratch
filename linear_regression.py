# -*- coding: utf-8 -*-
"""
Linear Regression from Scratch
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Simulate Data
x = np.random.exponential(scale = 100, size = 200)
y = 250 + 10*x + np.random.normal(loc = 10, scale = 5, size = 200)

# Random Initialization of Parameters
theta_1 = np.random.random(1)
theta_2 = np.random.random(1)

# Predictions
y_hat = theta_1 + theta_2*x

# Loss Function
def loss_function(y, y_hat):
    return 0.5*np.mean((np.abs(y-y_hat))**2)

# Gradients of the loss function with respect to the parameters
# del_theta_1 = np.mean(y_hat - y)
# del_theta_2 = np.mean((y_hat - y)*x)

# Gradient Descent
learning_rate = 0.00005
n_iterations = 1000000
n_iteration = 0
ax = plt.axes()

while (n_iteration < n_iterations):
    y_hat = theta_1 + theta_2*x
    loss = loss_function(y, y_hat)
    del_theta_1 = np.mean(y_hat - y)
    del_theta_2 = np.mean((y_hat - y)*x)
    theta_1 = theta_1 - learning_rate*del_theta_1
    theta_2 = theta_2 - learning_rate*del_theta_2
    n_iteration = n_iteration + 1
    if n_iteration%10000 == 0:
        ax.scatter(n_iteration, loss)
        plt.draw()


    
    