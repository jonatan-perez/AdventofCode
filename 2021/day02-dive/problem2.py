with open("2021/day02-dive/input.txt") as f:
    input = [line.split() for line in f]

def calc_pos(input):
    position = [0, 0, 0] #horiz, depth, aim
    for instr in input:
        direction = instr[0]
        value = int(instr[1])
        if direction == "forward": 
            position[0] += value
            position[1] += (position[2] * value)
        elif direction == "down": 
            position[2] += value
        elif direction == "up":
            position[2] -= value
    return position[0] * position[1]

print(calc_pos(input))