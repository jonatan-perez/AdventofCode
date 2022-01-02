import sys

def get_inputs(file):
    with open(f"2021/day15-chiton/{file}.txt") as f:
        cavern = [[int(num) for num in line.rstrip("\n")] for line in f]

    start = (0, 0)
    exit = (len(cavern) - 1, len(cavern[0]) - 1)
    return cavern, start, exit

def create_structs(cavern, start):
    #create list for unvisited positions and dictionary with each position's risk value
    cavern_risk_values = {}
    unvisited = []
    for y in range(len(cavern)):
        for x in range(len(cavern[0])):
            unvisited.append((y, x))
            cavern_risk_values[(y, x)] = cavern[y][x]

    #create dict to keep track of lowest_risk path and mark start as 0 since it is not counted 
    lowest_risk = {}
    max_val = sys.maxsize
    for pos in unvisited:
        lowest_risk[pos] = max_val
    lowest_risk[start] = 0

    return cavern_risk_values, lowest_risk, unvisited

prev_pos = {} #dict to keep track of how you're getting to each position

def getNeighbors(curr_pos, cavern):
    """
    Given a tuple of (y, x) returns neighbors (up, down, right, left) within bounds of the cavern
    """
    neighbors = []
    max_y = len(cavern)
    max_x = len(cavern[0])

    y = curr_pos[0]
    x = curr_pos[1]
    yy = [-1, 0, 1]
    xx = [-1, 0, 1]
    for col in yy:
        for row in xx:
            if abs(col) != abs(row):
                new_y = y + col
                new_x = x + row
                if (new_y >= 0 and new_y < max_y) and (new_x >= 0 and new_x < max_x) and (new_y, new_x):
                    neighbors.append((new_y, new_x))

    return neighbors


#dijkstra's algo
def dijkstras(cavern, unvisited, lowest_risk, cavern_risk_values):
    while len(unvisited) > 0:
        curr_lowest_risk = None
        for pos in unvisited:
            if curr_lowest_risk == None:
                curr_lowest_risk = pos
            elif lowest_risk[pos] < lowest_risk[curr_lowest_risk]:
                curr_lowest_risk = pos
        neighbors = getNeighbors(curr_lowest_risk, cavern)
        for neighbor in neighbors:
            tent_risk = lowest_risk[curr_lowest_risk] + cavern_risk_values[neighbor]
            if tent_risk < lowest_risk[neighbor]:
                lowest_risk[neighbor] = tent_risk
                prev_pos[neighbor] = curr_lowest_risk
        unvisited.remove(curr_lowest_risk)
    return lowest_risk

#prints out path backwards for debugging purposes
def printPath(start, exit):
    if exit == start:
        return
    else:
        previous = prev_pos[exit]
        print(previous)
        printPath(previous)

def get_answer(file):
    cavern, start, exit = get_inputs(file)
    cavern_risk_values, lowest_risk, unvisited = create_structs(cavern, start)
    lowest_risk = dijkstras(cavern, unvisited, lowest_risk, cavern_risk_values)
    return lowest_risk[exit]

print(get_answer("input"))
