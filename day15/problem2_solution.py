import sys

with open("input.txt") as f:
    cavern = [[int(num) for num in line.rstrip("\n")] for line in f]

def expand(row):
    return [(val + 1 if val < 9 else 1) for val in row]

for row in cavern:
    row_copy = row.copy()
    for i in range(4):
        row_copy = expand(row_copy)
        row.extend(row_copy)

new_rows = cavern.copy()

for i in range(4):
    new_rows = [expand(row) for row in new_rows]
    cavern.extend(new_rows)

start = (0, 0)
exit = (len(cavern) - 1, len(cavern[0]) - 1)

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

prev_pos = {} #dict to keep track of how you're getting to each position

def getNeighbors(curr_pos):
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
#extremely inefficient solution solution for larger grid. Should implement priority queue
while len(unvisited) > 0:
    if len(unvisited) % 100 == 0:
        print(len(unvisited))
    curr_lowest_risk = None
    for pos in unvisited:
        if curr_lowest_risk == None:
            curr_lowest_risk = pos
        elif lowest_risk[pos] < lowest_risk[curr_lowest_risk]:
            curr_lowest_risk = pos
    neighbors = getNeighbors(curr_lowest_risk)
    for neighbor in neighbors:
        tent_risk = lowest_risk[curr_lowest_risk] + cavern_risk_values[neighbor]
        if tent_risk < lowest_risk[neighbor]:
            lowest_risk[neighbor] = tent_risk
            prev_pos[neighbor] = curr_lowest_risk
    unvisited.remove(curr_lowest_risk)

#prints out path backwards for debugging purposes
def printPath(exit):
    if exit == start:
        return
    else:
        previous = prev_pos[exit]
        print(previous)
        printPath(previous)

print("answer: ", lowest_risk[exit])