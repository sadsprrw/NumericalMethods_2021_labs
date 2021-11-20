import math
import numpy as np
import matplotlib.pyplot as plt

y = lambda x: np.sin(x)


def chebyshev_s_nodes(k, pi=3.14):
    return math.cos((2 * k + 1) * pi / (n * 2))


def wki(k, ik, x):
    result = 1
    for j in range(ik):
        if j != k:
            result *= (x[k] - x[j])
    return result


def wi(ik, x):
    result = "1"
    for j in range(ik):
        result += " * (x - " + str(x[j]) + ")"
    return result


def ai(x, ik):
    result = 0
    for j in range(0, ik):
        result += y(x[j])/wki(j, ik, x)
    return result


def lagrangian_polynomial(x, yk, ik):
    result = str(yk)
    for j in range(len(x)):
        if j != ik:
            result += " * " + "(x - " + str(x[j]) + ") / (" + str(x[ik] - x[j]) + ")"
    return result


def newton_polynomial(x, yk):
    result = "0"
    for j in range(1, len(x)-1):
        result += " + " + str(ai(x, j)) + " * " + wi(j-1, x)
    return result


n = 9
xn = [0]*n
yn = [0]*n
for i in range(n):
    xn[i] = chebyshev_s_nodes(i)
    yn[i] = y(xn[i])

a = newton_polynomial(xn, yn)
nInterpolationStr = "lambda x: " + a
lInterpolationStr = "lambda x: 0"

for i in range(len(xn)):
    lInterpolationStr += " + " + lagrangian_polynomial(xn, yn[i], i)

nInterpolation = eval(nInterpolationStr)
lInterpolation = eval(lInterpolationStr)
xi = np.linspace(-3.5, 4, 1000)
fig, axis = plt.subplots(2)
axis[0].plot(xi, lInterpolation(xi))
axis[0].plot(xi, y(xi))

axis[1].plot(xi, nInterpolation(xi))
axis[1].plot(xi, y(xi))

plt.show()

