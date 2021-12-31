with open("input.txt") as f:
    lines = [line.rstrip("\n").split(" | ") for line in f]
    inputs = [line[0] for line in lines]
    outputs = [line[1].split(" ") for line in lines]

count = 0
for output in outputs:
    for value in output:
        unique_number = [2, 4, 3, 7]
        if len(value) in unique_number:
            count += 1

print(count)