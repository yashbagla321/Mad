import numpy as np
import matplotlib.pyplot as plt
import random


n = int(input())
k = int(n**0.5)

X = []
Y = []


for i in range(n):
    X.append(random.random())
    Y.append(random.random())


print(X, Y)

fig = plt.figure()
ax = fig.gca()
plt.scatter(X, Y)
plt.axis([0, 1, 0, 1])
ax.set_xticks(np.arange(0, 1., (1/k)))
ax.set_yticks(np.arange(0, 1., (1/k)))
plt.grid(True)
plt.show()