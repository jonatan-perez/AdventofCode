with open("2022/day01-calorie-counting/input.txt") as f: 
    elf_calories = []
    curr_elf = []
    for line in f:
        if line == '\n':
            elf_calories += [sum(curr_elf)]
            curr_elf = []
        else:
            curr_elf += [int(line.rstrip('\n'))]
    
    elf_calories += [sum(curr_elf)]

elf_calories.sort(reverse = True)

print(sum(elf_calories[:3]))