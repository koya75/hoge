import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x)
    return exp_x/sum_exp_x

def tanh(x):
    exp_x = np.exp(x)
    exp__x = np.exp(-x)
    return (exp_x-exp__x)/(exp_x+exp__x)

x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = softmax(x)
y3 = tanh(x)

plt.plot(x, y1,label = 'sigmoid')
plt.plot(x, y2,label = 'softmax')
plt.plot(x, y3,label = 'tanh')
plt.legend()
plt.xlabel('input')
plt.ylabel('output')
plt.ylim(-1.2, 1.2)
plt.show()
