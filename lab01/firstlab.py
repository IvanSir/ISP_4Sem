import numpy

WorkAr = [
    [3.53, 0.81, 1.87, 0.92, -0.53, 4.2],
    [-0.53, 3.53, 0.81, 1.87, 0.92, 4.2],
    [2.12, -0.53, 3.53, 0.81, 1.87, 4.2],
    [0.67, 2.12, -0.53, 3.53, 0.81, 4.2],
    [0.81, 0.67, 2.12, -0.53, 3.53, 4.2]
]


def swap_lines(array, i, j):
    """Swapping line i with line j"""
    array[i], array[j] = array[j], array[i]


def multiplier(array, i, j):
    """Returns Multiplier for making element array[j][k] = 0"""
    k = 0
    while array[j][k] == 0 or k == 5 or array[i][k] == 0:
        k += 1
    return -array[j][k] / array[i][k]


def combine_rows(array, i, j, multiple):
    """Multiple * line i and add to line j"""
    for k in range(0, 6):
        array[j][k] = array[j][k] + array[i][k] * multiple
        k += 1


def triangular_matrix(array):
    """Changes your matrix to the upper_triangular type"""
    i = 0
    while i < 4:
        k = 1
        counter = 0
        while k < 5 - i:
            multiple = multiplier(array, i, i + 1)
            j = i + 1
            if array[j][i] != 0:
                combine_rows(array, i, j, multiple)
            j += 1
            swap_lines(array, i + 1, 4 - counter)
            counter += 1
            k += 1
        i += 1


def find_roots(array):
    """Solves SLAE and returns array of roots"""
    x = [0, 0, 0, 0, 0]
    i = 4
    k = 4
    while i >= 0:
        j = 5
        sum_xelements = array[i][j]
        while j > 0:
            if array[i][j - 2] == 0 or j - 2 < 0:
                break
            sum_xelements -= array[i][j - 1] * x[j - 1]
            j -= 1
        x[k] = sum_xelements / array[i][j - 1]
        k -= 1
        i -= 1
    return x


def gauss_solution(array):
    """Creates upper triangular matrix and solves"""
    triangular_matrix(array)
    return find_roots(array)


numpy.set_printoptions(precision=3)
print("Matrix: \n", numpy.array(WorkAr))
print("Roots = ", numpy.array(gauss_solution(WorkAr)))
print(gauss_solution.__doc__)
