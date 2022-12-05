from string import ascii_letters
from os import linesep
from collections import Counter


def solve(f):
    intersection = []
    for line in f.read().split(linesep):
        ascii = {c: (ascii_letters.index(c) + 1) for c in line}
        firstpart, secondpart = line[: len(line) // 2], line[len(line) // 2 :]
        intersection.append(ascii[set(firstpart) & set(secondpart)])
    return sum(intersection)


def solve2(f):
    sum = 0
    try:
        iterator = iter(f.read().split())
        while True:
            first, second, third = next(iterator), next(iterator), next(iterator)
            sum += ascii_letters.index(set(first).intersection(second, third).pop()) + 1
    except StopIteration:
        return sum


filename = "data/day3.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
