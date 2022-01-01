with open("2021/day02-dive/input.txt") as f:
    input = [line.split() for line in f]

def calc_pos(input):
    position = [0, 0] 
    for instr in input:
        direction = instr[0]
        value = int(instr[1])
        if direction == "forward": 
            position[0] += value
        if direction == "down": 
            position[1] += value
        if direction == "up":
            position[1] -= value
    return position[0] * position[1]

print(calc_pos(input))