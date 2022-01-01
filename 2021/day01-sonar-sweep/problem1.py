with open("input.txt") as f: 
    numbers = [int(line) for line in f]
def count_increases(numbers):
    larger_measurements = 0
    for index in range(len(numbers) - 1):
        if  numbers[index + 1] > numbers[index]:
            larger_measurements += 1
    return larger_measurements

print(count_increases(numbers))
