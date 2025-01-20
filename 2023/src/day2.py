from functools import reduce


def solve(f):
    ans = 0
    for i, game in enumerate(f.read().splitlines()):
        game_split = game.strip().split(": ")[1].split("; ")
        for round in game_split:
            round_base = {"red": 0, "green": 0, "blue": 0}
            for cube in round.split(", "):
                j, color = cube.split()
                round_base[color] = int(j)
            if (
                (round_base["red"] > 12)
                | (round_base["green"] > 13)
                | (round_base["blue"] > 14)
            ):
                break
        else:
            ans += i + 1
    return ans


def solve2(f):
    ans = 0
    for i, game in enumerate(f.read().splitlines()):
        game_split = game.strip().split(": ")[1].split("; ")
        round_base = {"red": 0, "green": 0, "blue": 0}
        for round in game_split:
            for cube in round.split(", "):
                j, color = cube.split()
                if round_base[color] < int(j):
                    round_base[color] = int(j)
        ans += reduce(lambda x, y: x * y, list(round_base.values()), 1)
    return ans


filename = "../data/day2.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
