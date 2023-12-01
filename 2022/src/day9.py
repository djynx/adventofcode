import os
from math import dist, sqrt


def solve(f) -> int:
    visited = set([(0, 0)])
    tail = [0, 0]
    head = [0, 0]
    for line in f.read().splitlines():
        direction, steps = line.split()
        for _ in range(int(steps)):
            stepX = 1 if direction == "R" else -1 if direction == "L" else 0
            stepY = 1 if direction == "U" else -1 if direction == "D" else 0
            head[0] += stepX
            head[1] += stepY
            if dist(tail, head) > sqrt(2):
                distX = head[0] - tail[0]
                distY = head[1] - tail[1]
                if distX == 0:
                    tail[1] += distY // 2
                elif distY == 0:
                    tail[0] += distX // 2
                else:
                    tail[0] += 1 if distX > 0 else -1
                    tail[1] += 1 if distY > 0 else -1
            visited.add(tuple(tail))  # type: ignore
    return len(visited)


def solve2(f):
    visited = set([(0, 0)])
    rope = [[0, 0] for _ in range(10)]
    for line in f.read().splitlines():
        direction, steps = line.split()
        for _ in range(int(steps)):
            stepX = 1 if direction == "R" else -1 if direction == "L" else 0
            stepY = 1 if direction == "U" else -1 if direction == "D" else 0
            rope[0][0] += stepX
            rope[0][1] += stepY
            for i in range(len(rope) - 1):
                head = rope[i]
                tail = rope[i + 1]
                if dist(tail, head) > sqrt(2):
                    distX = head[0] - tail[0]
                    distY = head[1] - tail[1]
                    if distX == 0:
                        tail[1] += distY // 2
                    elif distY == 0:
                        tail[0] += distX // 2
                    else:
                        tail[0] += 1 if distX > 0 else -1
                        tail[1] += 1 if distY > 0 else -1
            visited.add(tuple(rope[-1]))  # type: ignore
    return len(visited)


day = __file__.split(os.sep)[-1].split(os.extsep)[0]
path = os.path.join(os.path.dirname(__file__), f"../data/{day}.input")

mode = "r"
f = open(path, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
