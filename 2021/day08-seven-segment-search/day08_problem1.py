with open("2021/day08-seven-segment-search/input.txt") as f:
    lines = [line.rstrip("\n").split(" | ") for line in f]
    outputs = [line[1].split(" ") for line in lines]

def count_simple_digits(outputs):
    count = 0
    for output in outputs:
        for value in output:
            unique_number = [2, 4, 3, 7]
            if len(value) in unique_number:
                count += 1
    return count
print(count_simple_digits(outputs))