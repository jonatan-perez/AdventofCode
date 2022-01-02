def calc_total(file):
    open_chunks = "([{<"
    corrupted = []
    stack = []
    with open(f"2021/day10-syntax-scoring/{file}.txt") as f:
        for line in f:
            for char in line:
                if char in open_chunks:
                    stack.append(char)
                else: 
                    last_char = stack.pop()
                    if (char == ")" and last_char != "(") or (char == "]" and last_char != "[") or (char == "}" and last_char != "{") or (char == ">" and last_char != "<"):
                        corrupted.append(char)
                        break

    total = 0
    for corr in corrupted: 
        if corr == ")":
            total += 3
        elif corr == "]":
            total += 57
        elif corr == "}":
            total += 1197
        elif corr == ">":
            total += 25137

    return total

print(calc_total("input"))
