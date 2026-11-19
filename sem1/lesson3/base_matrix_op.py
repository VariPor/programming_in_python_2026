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
import re

class myException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Ошибка моего модуля: {message}")


class measureTimeException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(f"Ошибка измерения времени: {message}")


def calc_time_print_name(func):
    def wrapper(*args, **kwargs):
        try:
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            if end < start:
                raise measureTimeException(
                    f"время выполнения функции {func.__name__} отрицательно {end - start}"
                )
            print(func.__name__, "Затрачено времени:", end - start)
            return result
        except measureTimeException as e:
            print(e)
            return result
        except Exception as e:
            print(e)

    return wrapper


@calc_time_print_name
def mul_vectors(vector1, vector2):
    n = len(vector2)
    res = 0
    if len(vector1) != n:
        raise myException(f"разные размерности векторов {len(vector1)} {n}")
    for i in range(len(vector1)):
        res += vector1[i] * vector2[i]
    return res


@calc_time_print_name
def mul_matrix(a, b):
    res = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    if len(a[0]) != len(b):
        raise myException(
            f"матрицы с размерностями {len(a)}x{len(a[0])}, {len(b)}x{len(b[0])} невозможно перемножить"
        )
    for i in range(len(a)):
        for j in range(len(b[0])):
            row = [b[k][j] for k in range(len(b))]
            # print(a[i], row)
            res[i][j] = mul_vectors(a[i], row)
    return res


@calc_time_print_name
def mul_matrix_vector(matrix, vector):
    vector = [[i] for i in vector]
    return mul_matrix(matrix, vector)


@calc_time_print_name
def find_trace(matrix):
    if len(matrix) != len(matrix[0]):
        raise myException("попытка найти след неквадратной матрицы")
    res = 0
    for i in range(len(matrix)):
        res += matrix[i][i]
    return res


@calc_time_print_name
def calc_hist(vector, steps_num, interval):
    if steps_num <= 0:
        raise myException(f"Неположительное число шагов для гистограммы: {steps_num}")
    if interval[0] >= interval[1]:
        raise myException(f"Интервал задан неправильно {interval[0]}, {interval[1]}")
    step = (interval[1] - interval[0]) / steps_num
    res = [0 for _ in range(steps_num)]
    for i in range(len(vector)):
        # print(int((vector[i] - interval[0]) // step))
        t = int((vector[i] - interval[0]) // step)
        res[t if t < steps_num else steps_num - 1] += 1
    return res


@calc_time_print_name
def vector_filtering(vector, core):
    if len(core) > len(vector):
        raise myException("размер ядра свёртки больше вектора")
    res = []
    for i in range(len(vector) - len(core) + 1):
        res.append(mul_vectors(vector[i : i + len(core)], core))
    return res


@calc_time_print_name
def read_write_file(s, mode, file_name):
    try:
        '''if file_name.split(".")[-1] == "bin":
            raise myException("попытка прочитать или записать бинарный файл")'''
        match = re.search(r".[a-z]+$", file_name)
        if match is None:
            print(f"WARNING: no extension - {file_name}")
        else:
            ext = match.group()
            if ext == ".bin":
                raise myException("попытка прочитать или записать бинарный файл")
            if ext in (".png", ".jpeg", ".jpg"):
                print(f"WARNING: read/write to image file {file_name}")
            if ext == ".json":
                print("write to json file")
        if mode == "r":
            with open(file_name, "r") as f:
                return f.read()
        if mode == "w":
            with open(file_name, "w") as f:
                f.write(s)
    except FileNotFoundError:
        print(f"файл {file_name} не найден")
    except FileExistsError:
        print(f"файл {file_name} уже существует")
    except Exception as e:
        print(e)
        


if __name__ == "__main__":
    print(mul_vectors([1, 1], [2, 3]))
    print(mul_matrix([[1, 2], [3, 4]], [[1, 3], [0, 0]]))
    print(mul_matrix_vector([[1, 2], [3, 4]], [1, 2]))
    print(find_trace([[1, 2], [3, 4]]))
    print(calc_hist([1, 2, 3, 6, 10], 10, (0, 10)))
    print(vector_filtering([1, 2, 3, 4, 5], [-1, 0, 1]))
    read_write_file("something", "w", "buff")
    print(read_write_file("", "r", "base_matrix_op.py"))
