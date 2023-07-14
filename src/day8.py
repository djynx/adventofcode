def solve(f):
    t = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            tree = grid[row][column]
            if all(grid[row][x] < tree for x in range(column)) or \
                all(grid[row][x] < tree for x in range(column + 1, len(grid[row]))) or \
                    all(grid[x][column] < tree for x in range(row)) or \
                    all(grid[x][column] < tree for x in range(row + 1, len(grid))):
                t += 1
    return t


def solve2(f):
    t = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            tree = grid[row][column]
            L = R = T = B = 0
            for x in range(column - 1, -1, -1):
                L += 1
                if grid[row][x] >= tree:
                    break
            for x in range(column + 1, len(grid[row])):
                R += 1
                if grid[row][x] >= tree:
                    break
            for x in range(row - 1, -1, -1):
                T += 1
                if grid[x][column] >= tree:
                    break
            for x in range(row + 1, len(grid)):
                B += 1
                if grid[x][column] >= tree:
                    break
            t = max(t, T * B * L * R)
    return t


filename = "../data/day8.input"
mode = "r"
f = open(filename, mode)
grid = [list(map(int, line)) for line in f.read().splitlines()]
print(solve(f))
f.seek(0, 0)
print(solve2(f))
