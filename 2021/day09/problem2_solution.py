with open("input.txt") as f:
    lines = [line.rstrip("\n") for line in f]
    vents = [[int(num) for num in line] for line in lines]

low_points = []

xx = [-1, 0, 1]
yy = [-1, 0, 1]
y_length = len(vents)
x_length = len(vents[0])
for y in range(y_length):
    for x in range(x_length):
        curr_vent = vents[y][x]
        lowest = []
        for row in xx:
            for col in yy:
                new_x = x + row
                new_y = y + col
                if 0 <= new_x < x_length and 0 <= new_y < y_length and row != col:
                    if curr_vent < vents[new_y][new_x]:
                        lowest.append(True)
                    else:
                        lowest.append(False)
        if all(lowest):
            low_points.append([y, x])


def findBasins(y, x, checked):
    if (y < 0 or y >= y_length) or (x < 0 or x >= x_length) or [y, x] in checked:
        return 0
    elif vents[y][x] == 9:
        return 0
    else:
        checked.append([y , x])
        return 1 + findBasins(y + 1, x, checked) + findBasins(y - 1, x, checked) + findBasins(y, x + 1, checked) + findBasins(y, x - 1, checked)

basin_sizes = []
for points in low_points:
    y = points[0]
    x = points[1]
    basin_sizes.append(findBasins(y, x, []))

largest = sorted(basin_sizes, reverse=True)
print(largest[0] * largest[1] * largest[2])
