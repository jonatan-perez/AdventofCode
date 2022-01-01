with open("2021/day01-sonar-sweep/input.txt") as f: 
    numbers = [int(line) for line in f]

def larger_sums(numbers):
    larger_measurements = 0
    for index in range(len(numbers) - 3):
        if  numbers[index + 3] > numbers[index]:
            larger_measurements += 1
    return larger_measurements
print(larger_sums(numbers))