with open("input.txt") as f:
    marks = [line.replace("\n", "") for line in f]
    for i in range(len(marks)):
        if marks[i] == "":
            dot_strings = marks[:i]
            instructions = marks[i + 1: len(marks)]
dots = []
curr_max_x = 0
curr_max_y = 0
for dot in dot_strings:
    dot_split = dot.split(",")
    x = int(dot_split[0])
    y = int(dot_split[1])
    dots.append([x, y])
    if x > curr_max_x:
        curr_max_x = x
    if y > curr_max_y:
        curr_max_y = y

curr_max_x += 1
curr_max_y += 1
grid = [[0] * curr_max_x for i in range(curr_max_y)]

for dot in dots:
    x = dot[0]
    y = dot[1]
    grid[y][x] = 1 #lists stack on each other so you first have to get y then x

instruction = instructions[0]
axis = instruction[11]
line = int(instruction[13:])
if axis == "y":
    temp = grid
    grid = temp[:line]
    discarded_grid = temp[line + 1:]
    reversed_disc_grid = discarded_grid[::-1]
    for y in range(len(reversed_disc_grid)): #reversed because you are folding
        for x in range(len(reversed_disc_grid[y])):
            if reversed_disc_grid[y][x] == 1:
                grid[y][x] = 1

elif axis == "x":
    temp = grid
    grid = []
    discarded_grid = []
    reversed_disc_grid = []
    for row in temp:
        grid.append(row[:line])
        discarded_grid.append(row[line + 1:])

    for row in discarded_grid:
        reversed_disc_grid.append(row[::-1])

    for y in range(len(reversed_disc_grid)): #reversed because you are folding
        for x in range(len(reversed_disc_grid[y])):
            if reversed_disc_grid[y][x] == 1:
                grid[y][x] = 1

total = 0
for row in grid:
    total += sum(row)
    
print(total)

