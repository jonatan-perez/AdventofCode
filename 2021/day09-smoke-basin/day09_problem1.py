with open("2021/day09-smoke-basin/input.txt") as f:
    lines = [line.rstrip("\n") for line in f]
    vents = [[int(num) for num in line] for line in lines]

def calc_risk_level(vents):
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
                    #avoid where row == col because not checking diag
                    if 0 <= new_x < x_length and 0 <= new_y < y_length and row != col: 
                        if curr_vent < vents[new_y][new_x]:
                            lowest.append(True)
                        else:
                            lowest.append(False)
            if all(lowest):
                low_points.append(vents[y][x])

    risk_level = [point + 1 for point in low_points]
    return sum(risk_level)
    
print(calc_risk_level(vents))