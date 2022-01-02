with open("2021/day06-lanternfish/input.txt") as f:
   lanternfish =  [int(i) for i in f.readline().strip("\n").split(",")]


def processOneDay(lanternfish, days):
    new_fish = []
    if days == 0:
        return len(lanternfish)
    for fish in lanternfish:
        if fish == 0:
            new_fish.append(8)
            new_fish.append(6)
        else: 
            new_fish.append(fish - 1)
    return processOneDay(new_fish, days - 1)

print(processOneDay(lanternfish, 80))