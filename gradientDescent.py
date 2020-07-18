import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

points = [(0.4, 1),(0.2, 0.9)]

def F(w):
    return sum((w* x - y)**2 for x, y in points)

def dF(w):
    return sum(2*(w* x - y) * x for x, y in points)
w = 0
eta = 0.01
N = 200
x = np.random.rand(N)
y = np.random.rand(N)
for t in range(N):
    points.append((x[t],y[t]))
print(points)
for t in range(1000):
    value = F(w)
    gradient = dF(w)
    w = w - eta * gradient
    print ("iteration {}: w= {} F(w) = {}".format(t, w, value))


# Plot
colors = (0,0,0)
area = np.pi*3
for t in range(N):
    plt.scatter(points[t][0], points[t][1], s=area, c=np.array([colors]), alpha=0.5)
    
p2y = w* 1
ax = plt.gca()
plt.plot([0,1],[0, p2y],color='k',marker='o')
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
plt.show()
