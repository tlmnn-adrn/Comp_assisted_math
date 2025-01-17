from sage.all import *
import numpy as np

def regression(points, dim:int=2):
    # Ax = b -> cannot be solved for x. But:
    # A^tAx = A^tb represents a projection into solution space, which has a solution, so:
    # x = (A^tA)^-1 * A^tb

    # for linear:
    # f(x) = c1 + c2x
    # Ax = b ->
    # (1 x1) * (c1) = (y1) 
    # (1 x2) * (c2)   (y2)

    AT = matrix([points[0]**i for i in range(dim)])
    A = AT.transpose()
    ATA = AT * A
    coeffs = (ATA.inverse()) * AT * vector(points[1])
    return np.polynomial.Polynomial(coeffs)

def trig_regression_ez(points):
    # f(x) = a + b * sin(x)
    xs = points[:,0]
    ys = points[:,1]
    AT = matrix([[1, sin(x)] for x in xs])
    A = AT.transpose()
    ATA = AT * A
    a, b = (ATA.inverse()) * AT * vector(ys)
    return lambda x: a + b * sin(x)

def trig_regression_med(points):
    # f(x) = a * sin(wx) + b * cos(ox)
    w, o = 1.2, -2.3
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    AT = matrix([[sin(w * x), cos(o * x)] for x in xs])
    A = AT.transpose()
    ATA = AT * A
    a, b = (ATA.inverse()) * AT * vector(ys)
    return lambda x: a + b * sin(x)
