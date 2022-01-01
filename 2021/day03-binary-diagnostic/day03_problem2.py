with open("2021/day03-binary-diagnostic/input.txt") as f:
    diag_report = [line.rstrip('\n') for line in f]

num_len = len(diag_report[0])

def calc_oxygen_rating(diag_report, num_len):
    oxygen_numbers = set(diag_report)
    for index in range(num_len): 
        if len(oxygen_numbers) == 1:
            break
        column = "".join(number[index] for number in oxygen_numbers)
        if column.count("1") >= column.count("0"):
            bit = "1"
        else: 
            bit = "0"
        oxygen_numbers = oxygen_numbers - set(number for number in oxygen_numbers if number[index] == bit)
    oxygen_rating = int(min(oxygen_numbers), 2)
    return oxygen_rating

def calc_co2_rating(diag_report, num_len):
    co2_numbers = set(diag_report)
    for index in range(num_len): 
        if len(co2_numbers) == 1:
            break
        column = "".join(number[index] for number in co2_numbers)
        if column.count("0") <= column.count("1"):
            bit = "0"
        else: 
            bit = "1"
        co2_numbers = co2_numbers - set(number for number in co2_numbers if number[index] == bit)
    co2_rating = int(min(co2_numbers), 2)
    return co2_rating

print(calc_oxygen_rating(diag_report, num_len) * calc_co2_rating(diag_report, num_len))