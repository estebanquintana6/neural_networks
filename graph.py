import numpy as np
import matplotlib.pyplot as plt

matrix = []
clusters = []

f = open('data', 'r')

for line in f:
    elements = line.split(',')
    coordenates = np.array(elements[0:-1], dtype=float)
    clusters.append(int(elements[-1]))

    matrix.append(coordenates)
    print(coordenates)

print(clusters)
colors = ['g.', 'r.']


index  = 0
for m in matrix:
    plt.plot(m[0], m[1], colors[clusters[index]], markersize=10)
    index = index+1

plt.show()