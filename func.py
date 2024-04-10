from numpy import pi
from numpy import exp
import matplotlib.pyplot as plt
import numpy as np

k = 1.38064852e-23
m = 4.76 * 10 ** -26

def vmax(t):
    return np.sqrt((2 * k * t) / (m))

def calc_maxwell(v, t, m):
    k1 = 2 * pi * v
    k2 = (m) / (2 * pi * k * t)
    k3 = exp(- (m * v ** 2) / (2 * k * t))
    return k1 * k2 * k3

def dist_btw(x1, y1, x2, y2):
    #print("DIST BETWEEN ", x1, y1, x2, y2, " IS ", np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    return (np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


print(vmax(300))

