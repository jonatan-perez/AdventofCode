from collections import Counter

with open("2021/day05-hydrothermal-venture/input.txt") as f:
    instructions = []
    for line in f:
        split_line = line.split(" -> ")
        start = [int(num) for num in split_line[0].split(",")]
        end = [int(num) for num in split_line[1].split(",")]
        instructions.append([start, end])


def calc_overlaps(instructions):
    vent_lines = Counter()

    for line in instructions:
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]

        if x1 == x2:
            if y1 < y2:
                start = y1
                end = y2
            else: 
                start = y2
                end = y1
            while start <= end:
                vent_lines[x1, start] += 1
                start +=1
        elif y1 == y2:
            if x1 < x2:
                start = x1
                end = x2
            else:
                start = x2
                end = x1
            while start <= end:
                vent_lines[start, y1] += 1
                start += 1

    total_overlap = 0
    for key in vent_lines.keys():
        if vent_lines[key] > 1:
            total_overlap += 1
    return total_overlap
print(calc_overlaps(instructions))