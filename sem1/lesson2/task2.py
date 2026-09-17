"""
Реализуйте функции:
Создающая вектор заданной длины N, заполнение – случайные числа от 0..1
Создающая матрицу MxN, заполнение – случайные числа 0..1
Умножающая матрицу на вектор (см. предыдущее ДЗ)
Печатающую матрицу
Печатающую вектор
Находящую сумму диагональных элементов матрицы
Реализующая двумерную свертку изображения.
"""


def funcA(N):
    import random

    res = []
    for _ in range(N):
        res.append(random.uniform(0, 1))
    return res


def funcB(M, N):
    import random

    res = []
    for _ in range(M):
        temp = []
        for _ in range(N):
            temp.append(random.uniform(0, 1))
        res.append(temp)
    return res


def funcC(matrix, vector):
    n = len(vector)
    res = []
    for i in range(len(matrix)):
        if len(matrix[i]) != n:
            print("разные размерности")
            return
        temp = 0
        for j in range(n):
            temp += matrix[i][j] * vector[j]
        res.append(temp)
    return res

def funcD(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:^4}", end=" ")
        print()
            
def funcF(vector):
    for i in range(len(vector)):
        print(f"{vector[i]:^4}")
        
        
def funcG(matrix):
    res = 0
    for i in range(len(matrix)):
        res += matrix[i][i]
    return res
        
def funcH(matrix, core):
    res = []
    for i in range(len(matrix) - len(core) + 1):
        temp = [0] * (len(matrix) - len(core) + 1)
        for j in range(len(matrix) - len(core) + 1):
            for k1 in range(len(core)):
                for k2 in range(len(core)):
                    temp[j] += matrix[i + k1][j + k2] * core[k1][k2]
        res.append(temp)
    return res

funcF(funcA(5))
funcD(funcB(5, 5))
funcF(funcC([[1, 2], [3, 4]], [1, 10]))
print(funcG([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
funcD(funcH([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 0], [0, 1]]))