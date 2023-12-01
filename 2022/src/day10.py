import os


def tick(cycle, x):
    cycle += 1
    if (cycle + 20) % 40 == 0:
        return (x * cycle, cycle)
    return (0, cycle)


def solve(f):
    instructions = f.read().splitlines()
    strength = 0
    X = 1
    cycle = 1
    for inst in instructions:
        if inst != "noop":
            _, V = inst.split()
            score, cycle = tick(cycle, X)
            strength += score
            X += int(V)
        score, cycle = tick(cycle, X)
        strength += score
    return strength


def solve2(f):
    return


day = __file__.split(os.sep)[-1].split(os.extsep)[0]
path = os.path.join(os.path.dirname(__file__), f"../data/{day}.input")

mode = "r"
f = open(path, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
