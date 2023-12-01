import os

# part1
def solve(f):
    array = []
    for elf in f.read().split(2 * os.linesep):
        array.append(sum(map(int, elf.split(os.linesep))))
    return max(array)


def solve2(f):
    array = []
    for elf in f.read().split(2 * os.linesep):
        array.append(sum(map(int, elf.split(os.linesep))))
    return sum(sorted(array)[-3:])


filename = "data/day1.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
