import numpy as np
import matplotlib.pyplot as plt
import random


n = int(input())
p_x = int(input())
p_y = int(input())

k = int(n**0.5)

def computeHaltonSequence(n, p):
    S = np.zeros(n)

    for i in range(n):
        i_tmp = i
        f = 1/p
        while i_tmp > 0:
            r = i_tmp % p
            q = (i_tmp)/p
            S[i] = S[i] + (f*r)
            i_tmp = q
            f = f/p
    
    return(S)


X = computeHaltonSequence(n, p_x)
Y = computeHaltonSequence(n, p_y)

print(X, Y)

fig = plt.figure()
ax = fig.gca()
plt.scatter(X, Y)
plt.axis([0, 1, 0, 1])
ax.set_xticks(np.arange(0, 1., (1/k)))
ax.set_yticks(np.arange(0, 1., (1/k)))
plt.grid(True)
plt.show()