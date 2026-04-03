import matplotlib.pyplot as plt
import numpy as np
import math
def f(x):
    return math.sin(x) + math.cos(x)
x = np.linspace(-10, 10, 1000)
y = [f(i) for i in x]
plt.plot(x, y)
plt.title('Graph of f(x) = sin(x) + cos(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

