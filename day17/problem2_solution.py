with open("input.txt") as f:
    target_area = f.readline()[13:]
    target_x, target_y = target_area.split(", ")
    target_x = [int(x) for x in target_x[2:].split("..")]
    target_y = [int(y) for y in target_y[2:].split("..")]

def processStep(x, y, velocity):
    x_vel = velocity[0]
    y_vel = velocity[1]
    new_x = x + x_vel
    new_y = y + y_vel
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1

    y_vel -= 1
    
    new_coordinates = [new_x, new_y]
    new_velocity = [x_vel, y_vel]
    return [new_coordinates, new_velocity]

potential_solutions = set()

min_y = target_y[0]
max_y = target_y[1]
min_x = target_x[0]
max_x = target_x[1]
for x_vel_orig in range(1, max_x + 1):
    for y_vel in range(min_y, max_x):
        x_vel = x_vel_orig #reset x_vel at end of each loop of y_vel because its modified below
        x, y, = 0, 0
        start_x = x_vel
        start_y = y_vel
        while x <= max_x and y >= min_y:
            vel = [x_vel, y_vel]
            vals = processStep(x, y, vel)
            x = vals[0][0]
            y = vals[0][1]
            x_vel = vals[1][0]
            y_vel = vals[1][1]
            if min_x <= x <= max_x and min_y <= y <= max_y:
                potential_solutions.add((start_x, start_y))

print(len(potential_solutions))

