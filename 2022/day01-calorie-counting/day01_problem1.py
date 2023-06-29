with open("2022/day01-calorie-counting/input.txt") as f: 
    max_calories = 0
    curr_elf = []
    for line in f:
        if line == '\n':
            max_calories = max(sum(curr_elf), max_calories)
            curr_elf = []
        else:
            curr_elf += [int(line.rstrip('\n'))]

print(max_calories)
