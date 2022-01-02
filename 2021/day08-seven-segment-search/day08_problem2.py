with open("2021/day08-seven-segment-search/input.txt") as f:
    lines = [line.rstrip("\n").split(" | ") for line in f]
    outputs = [line[1].split(" ") for line in lines]

def get_input_code(lines):
    return [line[0].split(" ") for line in lines]

def decodeInput(input_code):
    number_code = {}
    non_unique_values = []

    for value in input_code:
        sorted_value = "".join(sorted(value))
        if len(value) == 2:
            number_code[1] = sorted_value
        elif len(value) == 4:
            number_code[4] = sorted_value
        elif len(value) == 3:
            number_code[7] = sorted_value
        elif len(value) == 7:
            number_code[8] = sorted_value
        else:
            non_unique_values.append(sorted_value)
    leftover = []
    for sorted_value in non_unique_values:
        #get 2 and 9
        if len(sorted_value) == 5 and len([x for x in sorted_value if x not in number_code[4]]) == 3:
            number_code[2] = sorted_value
        elif len(sorted_value) == 6 and len([x for x in sorted_value if x not in number_code[4]]) == 2:
            number_code[9] = sorted_value
        else:
            leftover.append(sorted_value)

    for sorted_value in leftover:
        if len(sorted_value) == 5:
            if len([x for x in sorted_value if x not in number_code[1]]) == 3:
                number_code[3] = sorted_value
            else: 
                number_code[5] = sorted_value
        if len(sorted_value) == 6:
            if len([x for x in sorted_value if x not in number_code[1]]) == 4:
                number_code[0] = sorted_value
            else:
                number_code[6] = sorted_value
    return number_code

def add_output_values(input_code, outputs):
    total = 0
    for i in range(len(input_code)):
        current_number = ""
        number_code = decodeInput(input_code[i])
        code = {v: k for k, v in number_code.items()}
        for encoded_number in outputs[i]:
            sorted_number = "".join(sorted(encoded_number))
            current_number += str(code[sorted_number])
        total += int(current_number)
    return total
    
input_code = get_input_code(lines)
print(add_output_values(input_code, outputs))
