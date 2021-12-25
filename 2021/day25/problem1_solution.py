import copy

with open("input.txt") as f:
    grid = [[pos for pos in line.strip("\n")] for line in f]

def checkMoveValid(cucumber, grid, moveEast):
    h_lim = len(grid) - 1
    w_lim = len(grid[0]) - 1
    h, w = cucumber

    if moveEast:
        if w == w_lim:
            next_w = 0
        else:
            next_w = w + 1
        if grid[h][next_w] == ">" or grid[h][next_w] == "v":
            return False
    if moveEast == False:
        if h == h_lim:
            next_h = 0
        else:
            next_h = h + 1
        if grid[next_h][w] == ">" or grid[next_h][w] == "v":
            return False
    return True


height = len(grid)
width = len(grid[0])

no_moves = False
steps = 0
while no_moves == False:
    grid_copy = copy.deepcopy(grid)
    for h in range(height):
        for w in range(width):
            cucumber = (h, w)
            if grid[h][w] == ">" and checkMoveValid(cucumber, grid, True):
                grid_copy[h][w] = "."
                if w == width - 1:
                    grid_copy[h][0] = ">"
                else:
                    grid_copy[h][w + 1] = ">"
    grid_interm = copy.deepcopy(grid_copy)
    for h in range(height):
        for w in range(width):
            cucumber = (h, w)
            if grid_interm[h][w] == "v" and checkMoveValid(cucumber, grid_interm, False):
                grid_copy[h][w] = "."
                if h == height - 1:
                    grid_copy[0][w] = "v"
                else:
                    grid_copy[h + 1][w] = "v"
    steps += 1
    if grid == grid_copy:
        no_moves = True
    else:
        grid = copy.deepcopy(grid_copy)
print(steps)
