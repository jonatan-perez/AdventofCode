with open("input.txt") as f:
    instructions = [line.rstrip("\n").split(" ") for line in f]

#print out the differences for each set of instructions (14 total)
i = 0
for _ in range(14):
    div = int(instructions[i + 4][2])
    check = int(instructions[i + 5][2])
    offset = int(instructions[i + 15][2])
    print(check, offset)
    i += 18

# 13 14
# 12 8
# 11 5
# 0 4
# 15 10
# -13 13
# 10 16
# -9 5
# 11 6
# 13 13
# -14 6
# -3 7
# -2 13
# -14 3       

# PUSH input[0] + 14
# PUSH input[1] + 8
# PUSH input[2] + 5
# POP input[3] == popped_value - 0
# PUSH input[4] + 10
# POP input[5] == popped_value - 13
# PUSH input[6] + 16
# POP input[7] == popped_value - 9
# PUSH input[8] + 6
# PUSH input[9] + 13
# POP input[10] == popped_value - 14
# POP input[11] == popped_value - 3
# POP input[12] == popped_value - 2
# POP input[13] == popped_value - 14

# input[3] = input[2] + 5
# input[5] = input[4] - 3
# input[7] = input[6] + 7
# input[10] = input[9] - 1
# input[11] = input[8] + 3
# input[12] = input[1] + 6
# input[13] = input[0] + 0

#LARGEST VALID MODEL_NUMBER: 93499629698999
#SMALLEST VALID MODEL_NUMBER: 11164118121471
