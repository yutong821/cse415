from EightPuzzle import *


def h(s):
    c = 0
    listb = s.b

    for i, t1 in enumerate(listb):
        for j, t2 in enumerate(t1):
            if t2 == 0:
                continue
            else:
                row = (t2) // 3
                col = (t2) % 3
                c += abs(row - i) + abs(col - j)
    return c
