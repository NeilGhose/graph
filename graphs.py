import matplotlib.pyplot as plt
import numpy as np

def draw_graph(n, size = 1, length = 100):
    x = [i for i in range(length)]
    y = [[0] for i in range(n)]
    y.append( np.random.uniform(-size/100, size/100, size=length) )

    for p in range(1, length):
        for row in range(n):
            y[n-row-1].append( y[n-row-1][p-1] + y[n-row][p] )

    plt.plot(x,y[0])

    plt.show()


for t in range(10):
    draw_graph(t)
