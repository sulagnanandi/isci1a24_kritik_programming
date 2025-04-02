import numpy as np
import matplotlib.pyplot as plt


def normal_distribution(mean, variance, x):
    return (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-(x - mean) ** 2 / (2 * variance))


def integration(mean, variance, a, b):
    n = 100
    x = np.linspace(a, b, n + 1)
    delta_x = (b - a) / n
    probability = 0
    for i in range(n):
        probability += normal_distribution(mean, variance, x[i]) * delta_x
    return probability

# plotting
x = np.linspace(-50, 50, 10000)
mean = 0
variance = 1
y = []
for i in range(10000):
    y.append(normal_distribution(mean, variance, x[i]))
plt.plot(x, y)
plt.ylabel("PBM(sq)")
plt.legend()
plt.title("Approximate Solution Using Euler's Method")
plt.grid()
plt.show()
