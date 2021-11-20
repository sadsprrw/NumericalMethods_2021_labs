import math
import numpy
from scipy import optimize


def function1(x, y):
    return 5*x - 6 * y + 20 * math.log(x, 10) + 16


def function1_dx(x, y):
    return 5 + 20 / x


def function1_dy(x, y):
    return -6


def function2(x, y):
    return 2*x + y - 10 * math.log(y, 10) - 4


def function2_dx(x, y):
    return 2


def function2_dy(x, y):
    return 1 - 10/y


def function_sys(x):
    return [function1(x[0], x[1]), function2(x[0], x[1])]


def norm(z):
    max_z = abs(z[0])
    for i in z:
        if abs(i) > max_z:
            max_z = abs(i)
    return max_z


def modified_newton_method(b, size):
    eps = 0.0000001
    x0 = [1]*size
    a = numpy.array([[function1_dx(x0[0], x0[1]), function1_dy(x0[0], x0[1])],
                         [function2_dx(x0[0], x0[1]), function2_dy(x0[0], x0[1])]])
    f = numpy.array([function1(x0[0], x0[1]), function2(x0[0], x0[1])])
    x1 = x0 - numpy.linalg.inv(a) @ f

    while norm(x1 - x0) > eps:
        x0 = x1
        a = numpy.array([[function1_dx(x1[0], x1[1]), function1_dy(x1[0], x1[1])],
                         [function2_dx(x1[0], x1[1]), function2_dy(x1[0], x1[1])]])
        f = numpy.array([function1(x1[0], x1[1]), function2(x1[0], x1[1])])
        x1 = x0 - numpy.linalg.inv(a) @ f
    print(x1)
    print(f"{function1(x1[0], x1[1]):9.10f}")


def degree_method(a):
    eps = 0.1
    y0 = numpy.array([1.0]*4)
    y1 = a @ y0
    lmb1 = y1[0]
    y0 = a @ y1
    lmb2 = y0[0]/y1[0]
    while abs(lmb1 - lmb2) > eps:
        lmb1 = lmb2
        y1 = y0
        y0 = a @ y1
        lmb2 = y0[0]/y1[0]
    print(lmb2)


def func(x):
    return pow(x,3) - 3 * pow(x,2) - 17 * x + 22

A = numpy.array([[1, 2, 3, 4], [2, 1, 2, 3], [3, 2, -1, 2], [4, 3, 2, 1]])

print(func(1.5))