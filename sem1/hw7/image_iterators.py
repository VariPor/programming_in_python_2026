def linear_iterator(a):
    res = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            res.append((i, j))
    return res


def spiral_iterator(a):
    res = []
    vert = len(a) // 2
    hor = len(a[0]) // 2
    steps_vert = -1
    steps_hor = -1
    res.append((vert, hor))
    iterating = True
    while iterating:
        for i in range(0, steps_hor, steps_hor // abs(steps_hor)):
            hor += steps_hor // abs(steps_hor)
            # print("hor", hor, steps_hor, vert, steps_vert)
            if hor < 0 or hor >= len(a[0]):
                iterating = False
                break
            res.append((vert, hor))

        if not iterating:
            break

        steps_hor = (abs(steps_hor) + 1) * (-steps_hor // abs(steps_hor))

        for j in range(0, steps_vert, steps_vert // abs(steps_vert)):
            vert += steps_vert // abs(steps_vert)
            if vert < 0 or vert >= len(a):
                iterating = False
                break
            # print("vert", hor, steps_hor, vert, steps_vert)
            res.append((vert, hor))

        steps_vert = (abs(steps_vert) + 1) * (-steps_vert // abs(steps_vert))
    return res


def zigzag_iterator(a):
    res = []
    ind_cycle = [(0, 1), (1, -1), (1, 0), (-1, 1)]
    vert = 0
    hor = 0
    i_cycle = 0
    step_vert, step_hor = ind_cycle[i_cycle]
    res.append((vert, hor))
    rev = 1
    while True:
        if (
            vert + step_vert < 0
            or vert + step_vert >= len(a)
            or hor + step_hor < 0
            or hor + step_hor >= len(a[0])
        ):
            i_cycle += rev
            step_vert, step_hor = ind_cycle[i_cycle % 4]
        if (
            vert + step_vert < 0
            or vert + step_vert >= len(a)
            or hor + step_hor < 0
            or hor + step_hor >= len(a[0])
        ):
            if rev == -1:
                break
            rev = -1
            i_cycle -= 1
            i_cycle += rev
            step_vert, step_hor = ind_cycle[i_cycle % 4]
        vert += step_vert
        hor += step_hor
        res.append((vert, hor))

        if i_cycle == 0 or i_cycle == 2:
            i_cycle += rev
            step_vert, step_hor = ind_cycle[i_cycle % 4]

    return res


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print([a[ind[0]][ind[1]] for ind in linear_iterator(a)])
    print()
    print([a[ind[0]][ind[1]] for ind in spiral_iterator(a)])
    print()
    print([a[ind[0]][ind[1]] for ind in zigzag_iterator(a)])
    print()
