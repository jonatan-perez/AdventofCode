with open("input.txt") as f:
    diag_report = [line.rstrip('\n') for line in f]

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

print(gamma_dec * epsilon_dec)