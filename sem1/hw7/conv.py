from functools import partial
from image_iterators import linear_iterator, spiral_iterator, zigzag_iterator
import random


def conv(order, kernel, img):
    kh, kw = len(kernel), len(kernel[0])
    H, W = len(img), len(img[0])
    for i in range(H - kh + 1):
        yield [
            sum(kernel[a][b] * img[i + a][j + b] for a, b in order(kernel))
            for j in range(W - kw + 1)
        ]


def mse(A, B):
    flat = lambda M: [v for row in M for v in row]
    a, b = flat(A), flat(B)
    assert len(a) == len(b)
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)


random.seed(42)
img = [[random.randint(0, 255) for _ in range(9)] for _ in range(9)]


mean = ((1 / 9,) * 3,) * 3


orders = {
    "linear": linear_iterator,
    "spiral": spiral_iterator,
    "zigzag": zigzag_iterator,
}


ref = list(conv(linear_iterator, mean, img))
for oname, order in orders.items():
    res = list(conv(order, mean, img))
    print(f"  {oname:7s} MSE linear = {mse(ref, res):.3e}")
