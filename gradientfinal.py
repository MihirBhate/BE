# -*- coding: utf-8 -*-
"""graident_decent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zGfnyxIX0Wq7eSj5dYosEobizIV3uKpI
"""

import numpy as np
import matplotlib.pyplot as plt
import random

def f(x):
    return (x+3)**2

def df(x):
    return 2*(x+3)

def gradient_descent(start_x, learning_rate, num_iterations):
    x = start_x
    history_x= [x]
    for i in range(num_iterations):
        grad = df(x)
        x = x - learning_rate * grad
        history_x.append(x)
    return x,history_x

x = 2
learning_rate = 0.1
num_iterations = 50
min_x,history_x = gradient_descent(x, learning_rate, num_iterations)
print(min_x)

# plot graph of function, also of gradient descent

x = np.linspace(-10,10,100)
y = f(x)

plt.plot(x,y)

history_y = [f(i) for i in history_x]

plt.scatter(history_x,history_y)
plt.show()

# Plot the function and gradient descent steps
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='f(x) = (x+3)²')
plt.plot(history_x, history_y, 'ro-', label='Gradient Descent Steps')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Descent for f(x) = (x+3)²')
plt.legend()
plt.grid(True)

plt.show()

print(f"Local minimum found at x = {min_x:.4f}")
print(f"f(x) at minimum = {f(min_x):.4f}")

