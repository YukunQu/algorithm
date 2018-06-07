import numpy as np
from scipy.spatial.distance import pdist

x = np.random.random(10)
y = np.random.random(10)


X = np.vstack([x, y])
print(X)
XT = X.T
print(XT)
S = np.cov(X)
SI = np.linalg.inv(S)

n = XT.shape[0]
d1 = []
for i in range(0, n):
    for j in range(i + 1, n):
        delta = XT[i] - XT[j]
        d = np.sqrt(np.dot(np.dot(delta, SI), delta.T))
        d1.append(d)
print(d1)
print(len(d1))

d2=pdist(XT,'mahalanobis')

