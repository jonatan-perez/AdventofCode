with open("input.txt") as f: 
    numbers = [int(line) for line in f]

larger_measurements = 0
for index in range(len(numbers) - 3):
    if  numbers[index + 3] > numbers[index]:
        larger_measurements += 1
print(larger_measurements)