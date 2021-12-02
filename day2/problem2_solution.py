position = [0, 0, 0] #horiz, depth, aim

with open("input.txt") as f:
    for line in f:
        direction = line.split()[0]
        value = int(line.split()[1])
        if direction == "forward": 
            position[0] += value
            position[1] += (position[2] * value)
        elif direction == "down": 
            position[2] += value
        elif direction == "up":
            position[2] -= value

print(position[0] * position[1])