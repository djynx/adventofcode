from collections import defaultdict
from math import prod
import re


def find_special_neighbors(matrix, x, y, special_characters="!@#$%^&*()-+?_=,<>/"):
    num_rows, num_cols = len(matrix), len(matrix[0])
    for i in range(
        (0 if x - 1 < 0 else x - 1), (num_rows if x + 2 > num_rows else x + 2), 1
    ):
        for j in range(
            (0 if y - 1 < 0 else y - 1), (num_cols if y + 2 > num_cols else y + 2), 1
        ):
            if matrix[x][y] != matrix[i][j] and (matrix[i][j] in special_characters):
                return (i, j)


def solve(f):
    lines = f.read().split()
    ans = 0
    for idx, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            for digit in range(m.start(), m.end()):
                if find_special_neighbors(lines, idx, digit):
                    ans += int(line[m.start() : m.end()])
                    break
    return ans


def solve2(f):
    lines = f.read().split()
    gears = defaultdict(list)
    for idx, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            for digit in range(m.start(), m.end()):
                gear = find_special_neighbors(lines, idx, digit, "*")
                if gear:
                    gears[gear[0], gear[1]].append(int(m.group()))
                    break
    return sum(prod(gear) for gear in gears.values() if len(gear) == 2)


filename = "../data/day3.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
