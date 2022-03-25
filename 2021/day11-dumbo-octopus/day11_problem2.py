def process_step(flashes, octopi):
    for x in range(10):
        for y in range(10):
            octopi[x][y] += 1

    for x in range(10):
        for y in range(10):
            if octopi[x][y] > 9:
                flashes, octopi = flash(x, y, flashes, octopi)

    for x in range(10):
        for y in range(10):
            if octopi[x][y] == -1:
                octopi[x][y] = 0

    return flashes

def flash(x, y, flashes, octopi):

    flashes += 1
    octopi[x][y] = -1
    for row in [-1, 0, 1]:
        for col in [-1, 0, 1]:
            new_x = x + row
            new_y = y + col
            if 0 <= new_x < 10 and 0 <= new_y < 10 and octopi[new_x][new_y] != -1:
                octopi[new_x][new_y] += 1
                if octopi[new_x][new_y] >= 10:
                    flashes, octopi = flash(new_x, new_y, flashes, octopi)

    return flashes, octopi

def get_answer(file):
    with open(f"2021/day11-dumbo-octopus/{file}.txt") as f:
        levels = [line.replace("\n", "") for line in f]
        octopi = []
        for level in levels: 
            row = []
            for energy in level:
                row.append(int(energy))
            octopi.append(row)

    flashes = 0
    done = False
    steps = 0
    while not done:
        flashes += process_step(0, octopi)
        steps += 1
        flashes = sum([sum(line) for line in octopi])
        if flashes == 0:
            done = True

    return steps

