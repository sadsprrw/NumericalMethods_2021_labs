import math
import numpy


global result_matrix, result
result_matrix = [[0]*5]*4
result = []*4


def gauss_method(matrix, size):
    if size == 0:
        return
    global result_matrix
    a_max = -1000
    i_max = 0
    j_max = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])-1):
            if abs(matrix[i][j]) > a_max:
                a_max = abs(matrix[i][j])
                i_max = i
                j_max = j
    m = [0]*len(matrix)

    for i in range(len(m)):
        m[i] = -1 * matrix[i][j_max]/matrix[i_max][j_max]

    for i in range(len(matrix)):
        if i != i_max:
            for j in range(len(matrix[i])):
                matrix[i][j] = round(matrix[i][j] + matrix[i_max][j] * m[i], 2)

    result_matrix[i_max] = matrix[i_max]
    matrix[i_max] = [0]*len(matrix[i_max])
    gauss_method(matrix, size-1)


def solve_matrix(matrix):
    size = len(matrix)
    m1 = [[0]*size]*size
    v1 = [0]*size

    for i in range(size):
        v1[i] = matrix[i][size]
        m1[i] = matrix[i][:size]

    nm1 = numpy.array(m1)
    nv1 = numpy.array(v1)

    return numpy.linalg.solve(nm1, nv1)


def yakobi(A, b, eps=0.001):
    def check_conv():
        for i in range(0, A.shape[0]):
            sum = 0
            for j in range(0, A.shape[1]):
                if i != j:
                    sum += abs(A[i][j])
            if sum > abs(A[i][i]):
                return False
        return True

    if not check_conv():
        raise ValueError("Method does not converge")

    def calc_iter_process():
        iter_process = numpy.empty([4, 5])
        for i in range(0, A.shape[0]):
            arr = numpy.array(-A[i] / A[i][i])
            arr[i] = 0
            arr = numpy.append(arr, b[i] / A[i][i])
            iter_process[i] = arr
        return iter_process

    def calc_x_k(matrix, x_prev):
        return matrix @ x_prev

    iter = calc_iter_process()
    x_cur = numpy.array([0, 0, 0, 0])
    x_prev = numpy.array([100, 100, 100, 100])
    while numpy.abs(numpy.amax(x_cur - x_prev)) > eps:
        x1 = calc_x_k(iter, numpy.append(x_cur, 1))
        x_prev = x_cur
        x_cur = x1
    return x_cur


my_matrix = [[3, 1, -1, -1, 10],  [1, 10, -1, 1, 3],  [1, -1, 10, 1, -8],  [-1, 1, -1, 10, 10]]
gauss_method(my_matrix, 4)
result = solve_matrix(result_matrix)
print("Gauss result:")
print(result)

xA = numpy.array([[3, 1, -1, -1],  [1, 10, -1, 1],  [1, -1, 10, 1],  [-1, 1, -1, 10]])
xb = numpy.array([10, 3, -8, 10])
print("Yakobi result:")
print(yakobi(xA, xb).astype(numpy.float32))

xA_inv = numpy.linalg.inv(xA)
print("Number of conditionality is ", numpy.linalg.norm(xA, numpy.inf) * numpy.linalg.norm(xA_inv, numpy.inf))