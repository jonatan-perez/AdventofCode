with open("2021/day03-binary-diagnostic/input.txt") as f:
    diag_report = [line.rstrip('\n') for line in f]

def calc_power_consumption(diag_report):
    num_len = len(diag_report[0])

    gamma = ""
    epsilon = ""

    for index in range(num_len):
        column = "".join(number[index] for number in diag_report)
        if column.count("0") > column.count("1"):
            gamma += "1"
            epsilon += "0"
        else: 
            gamma += "0"
            epsilon += "1"

    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)
    return gamma_dec * epsilon_dec

print(calc_power_consumption(diag_report))