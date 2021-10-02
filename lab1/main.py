import math
import numpy


def function(x):
    return math.cos(x) + 3 * x + 1


def function_d(x):
    return 3 - math.sin(x)


def to_fixed(number):
    return f"{number:.{16}f}"


def results_output(results):
    print("---------------------------------------------------------")
    print("n \t| xn \t\t\t| f(xn) \t\t|")

    for i in range(len(results)):
        print("--------|-----------------------|-----------------------|")
        print(i, "\t|", results[i][0], "\t|", results[i][1], "\t|")


def dichotomy_method(a, b, eps):
    n = int(math.log2((b - a) / eps))
    results = []
    x = (a + b) / 2
    fx = function(x)

    results.append([x, to_fixed(fx)])

    if numpy.sign(a) == numpy.sign(fx):
        a = x
    else:
        b = x
    prev = x
    x = (a + b) / 2
    fx = function(x)
    results.append([x, to_fixed(fx)])

    while abs(x - prev) >= 2 * eps:
        if numpy.sign(a) == numpy.sign(fx):
            a = x
        else:
            b = x
        prev = x
        x = (a + b) / 2
        fx = function(x)
        results.append([x, to_fixed(fx)])

    print("-------------------Dichotomy Results---------------------")
    print("A priory mark: ", n)
    print("A posteriori mark: ", len(results))
    results_output(results)
    print("---------------------------------------------------------")


def relaxation_method(a, b, eps):
    fda = abs(function_d(a))
    fdb = abs(function_d(b))
    min1 = fdb if fda > fdb else fda
    max1 = fda if fda > fdb else fdb
    x = a
    prev = 100
    z0 = abs(x)
    q = (max1 - min1)/(max1 + min1)
    t0 = 2/(max1 + min1)
    n = int(numpy.log(abs(z0)/eps)/numpy.log(1/q)) + 1
    fx = function(x)

    results = [[x, to_fixed(fx)]]
    while abs(x - prev) >= 2*eps:
        prev = x
        x = prev - t0 * function(prev)
        fx = function(x)
        results.append([x, to_fixed(fx)])

    print("-------------------Relaxation Results---------------------")
    print("A priory mark: ", n)
    print("A posteriori mark: ", len(results))
    results_output(results)
    print("---------------------------------------------------------")


def main():
    a = -1*math.pi
    b = 0.5
    eps = 0.0001
    dichotomy_method(a, b, eps)
    relaxation_method(a, b, eps)



main()