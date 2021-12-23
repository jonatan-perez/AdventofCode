import math 

open_chunks = "([{<"
corrupted = []
stack = []
incomplete = []

with open("input.txt") as f:
    for line in f:
        stack = []
        for i in range(len(line)):
            char = line[i]
            if char in open_chunks:
                stack.append(char)
            else: 
                last_char = stack.pop()
                if (char == ")" and last_char != "(") or (char == "]" and last_char != "[") or (char == "}" and last_char != "{") or (char == ">" and last_char != "<"):
                    corrupted.append(char)
                    break
            if i == (len(line) - 1):
                stack.append(last_char) #need to readd last_char popped off that didn't have matching closing
                incomplete.append(stack)

point_totals = []

for stack in incomplete: 
    total = 0
    while len(stack) > 0:
        curr = stack.pop()
        if curr == "(":
            total = (total * 5) + 1
        elif curr == "[":
            total = (total * 5) + 2
        elif curr == "{":
            total = (total * 5) + 3
        elif curr == "<":
            total = (total * 5) + 4
    point_totals.append(total)

point_totals.sort()
middle = math.floor(len(point_totals) / 2)
print(point_totals[middle]) 

