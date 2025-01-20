import os


def solve(f):
    seed_to_location = {}
    f = f.read().split(2 * os.linesep)
    seeds = f[0].split(": ")[1].split()
    map = f[1].splitlines()[1:]
    for map in enumerate(f[1:]):
        for line in map:
            dst, src, _range = (int(n) for n in line.split())
            seed_to_location[(src, src + _range - 1)] = (dst, dst + _range - 1)


def solve2(f):
    return


filename = "../data/day5.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
