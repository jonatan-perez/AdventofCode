with open("2021/day07-the-treachery-of-whales/input.txt") as f:
    crab_positions = [int(x) for x in f.readline().rstrip('\n').split(",")]

def calc_least_fuel(crab_positions):
    mode_pos = max(set(crab_positions), key=crab_positions.count)
    mean_pos = round((sum(crab_positions) / len(crab_positions)))

    fuel_spent = sum([(((pos * pos) + pos) / 2) for pos in crab_positions])

    for i in range(min(mean_pos, mode_pos), max(mean_pos, mode_pos) + 1): 
        curr_fuel_spent = 0
        for pos in crab_positions:
            dist = abs((pos - i))
            curr_fuel_spent += (((dist * dist) + dist) / 2)
        if curr_fuel_spent < fuel_spent:
            fuel_spent = curr_fuel_spent
    return int(fuel_spent)

print(calc_least_fuel(crab_positions))