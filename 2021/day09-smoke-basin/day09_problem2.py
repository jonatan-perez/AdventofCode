with open("2021/day09-smoke-basin/input.txt") as f:
    lines = [line.rstrip("\n") for line in f]
    vents = [[int(num) for num in line] for line in lines]


def get_low_points(vents):
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
    return low_points


def findBasins(y, x, checked, y_length, x_length, vents):
    if (y < 0 or y >= y_length) or (x < 0 or x >= x_length) or [y, x] in checked:
        return 0
    elif vents[y][x] == 9:
        return 0
    else:
        checked.append([y , x])
        return (1 + findBasins(y + 1, x, checked, y_length, x_length, vents) + findBasins(y - 1, x, checked, y_length, x_length, vents) + 
        findBasins(y, x + 1, checked, y_length, x_length, vents) + findBasins(y, x - 1, checked, y_length, x_length, vents))

def get_largest_basins(low_points, vents):
    y_length = len(vents)
    x_length = len(vents[0])
    basin_sizes = []
    for points in low_points:
        y = points[0]
        x = points[1]
        basin_sizes.append(findBasins(y, x, [], y_length, x_length, vents))

    largest = sorted(basin_sizes, reverse=True)
    return largest[0] * largest[1] * largest[2]

low_points = get_low_points(vents)
print(get_largest_basins(low_points, vents))
