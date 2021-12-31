with open("input.txt") as f:
    levels = [line.replace("\n", "") for line in f]
    octopi = []
    for level in levels: 
        row = []
        for energy in level:
            row.append(int(energy))
        octopi.append(row)

flashes = 0

def process_step():
    global octopi
    for x in range(10):
        for y in range(10):
            octopi[x][y] += 1

    for x in range(10):
        for y in range(10):
            if octopi[x][y] > 9:
                flash(x, y)

    for x in range(10):
        for y in range(10):
            if octopi[x][y] == -1:
                octopi[x][y] = 0

def flash(x, y):
    global octopi
    global flashes

    flashes += 1
    octopi[x][y] = -1
    for row in [-1, 0, 1]:
        for col in [-1, 0, 1]:
            new_x = x + row
            new_y = y + col
            if 0 <= new_x < 10 and 0 <= new_y < 10 and octopi[new_x][new_y] != -1:
                octopi[new_x][new_y] += 1
                if octopi[new_x][new_y] >= 10:
                    flash(new_x, new_y)


for x in range(100):
    process_step()

print(flashes)
