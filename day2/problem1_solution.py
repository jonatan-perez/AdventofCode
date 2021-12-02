position = [0, 0] 

with open("input.txt") as f:
    for line in f:
        direction = line.split()[0]
        value = int(line.split()[1])
        if direction == "forward": 
            position[0] += value
        if direction == "down": 
            position[1] += value
        if direction == "up":
            position[1] -= value

print(position[0] * position[1])