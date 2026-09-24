"""
Умножение «матрица - матрица»
Умножение «матрица - вектор»
Расчет следа матрицы
Скалярное произведение двух векторов
Расчет гистограммы для вектора с изменяемым количеством квантов
Фильтрация вектора ядерным фильтром (например, [-1, 0, 1] – приближенное вычисление градиента данных)
чтение/запись данных в файл, из файла
"""

import time

def print_name(func):
    def wrapper(*args, **kwargs):
        if func.__name__ != "wrapper":
            print(func.__name__)
        result = func(*args, **kwargs)
        return result
    return wrapper

def calc_time_print_name(func):
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, "Затрачено времени:", end - start)
        return result
    return wrapper

@calc_time_print_name
def mul_vectors(vector1, vector2):
    n = len(vector2)
    res = 0
    if len(vector1) != n:
        print("разные размерности", len(vector1), n)
        return
    for i in range(len(vector1)):
        res += vector1[i] * vector2[i]
    return res

@calc_time_print_name
def mul_matrix(a, b):
    res = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            row = [b[k][j] for k in range(len(b))]
            print(a[i], row)
            res[i][j] = mul_vectors(a[i], row)
    return res

@calc_time_print_name
def mul_matrix_vector(matrix, vector):
    vector = [[i] for i in vector]
    return mul_matrix(matrix, vector)


@calc_time_print_name
def find_trace(matrix):
    res = 0
    for i in range(len(matrix)):
        res += matrix[i][i]
    return res

@calc_time_print_name
def calc_hist(vector, steps_num, interval):
    step = (interval[1] - interval[0]) / steps_num
    res = [0 for _ in range(steps_num)]
    for i in range(len(vector)):
        print(int((vector[i] - interval[0]) // step))
        t = int((vector[i] - interval[0]) // step)
        res[t if t < steps_num else steps_num-1] += 1
    return res

@calc_time_print_name
def vector_filtering(vector, core):
    res = []
    for i in range(len(vector) - len(core) + 1):
        res.append(mul_vectors(vector[i:i + len(core)], core))
    return res

@calc_time_print_name
def read_write_file(s, mode, file_name):
    if mode == "r":
        with open(file_name, "r") as f:
            return f.read()
    if mode == "w":
        with open(file_name, "w") as f:
            f.write(s)
            
if __name__ == "__main__":
    print(mul_vectors([1, 1], [2, 3]))
    print(mul_matrix([[1, 2], [3, 4]], [[1, 3], [0, 0]]))
    print(mul_matrix_vector([[1, 2], [3, 4]], [1, 2]))
    print(find_trace([[1, 2], [3, 4]]))
    print(calc_hist([1, 2, 3, 6, 10], 10, (0, 10)))
    print(vector_filtering([1, 2, 3, 4, 5], [-1, 0, 1]))
    read_write_file("something", "w", "buff")
    print(read_write_file("", "r", "base_matrix_op.py"))
        