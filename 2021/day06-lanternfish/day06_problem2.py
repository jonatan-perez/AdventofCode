def createLanternfishList(file):
    with open(file) as f:
        lanternfish = [0 for i in range(9)]
        fish_list =  [int(i) for i in f.readline().strip("\n").split(",")]
        for fish in fish_list:
            lanternfish[fish] += 1
    return lanternfish

def processOneDay(lanternfish, days_left):
    new_lanternfish = [0 for i in range(9)]
    if days_left == 0:
        return sum(lanternfish)
    else:
        for day in range(9):
            curr_fish = lanternfish[day]
            if day == 0:
                new_lanternfish[6] += curr_fish
                new_lanternfish[8] += curr_fish
                new_lanternfish[0] = 0
            else: 
                new_lanternfish[day - 1] += curr_fish

        return processOneDay(new_lanternfish, days_left - 1)

lanternfish = createLanternfishList("2021/day06-lanternfish/input.txt")
print(processOneDay(lanternfish, 256))