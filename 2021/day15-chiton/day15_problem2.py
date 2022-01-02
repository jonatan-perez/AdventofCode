import sys
import heapq
import itertools

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task, priority
    raise KeyError('pop from an empty priority queue')

def expand(row):
    return [(val + 1 if val < 9 else 1) for val in row]

def get_inputs(file):
    with open(f"2021/day15-chiton/{file}.txt") as f:
        cavern = [[int(num) for num in line.rstrip("\n")] for line in f]
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

    return cavern, start, exit


def create_pq(cavern, start):
    #create pq for unvisited positions and their value
    max_val = sys.maxsize
    for y in range(len(cavern)):
        for x in range(len(cavern[0])):
            add_task((y,x), max_val)
    #set start as 0 since not counted and add it to visited
    add_task(start, 0)
    visited = {}
    visited[start] = 0
    
    return visited

prev_pos = {} #dict to keep track of how you're getting to each position

def getNeighbors(curr_pos, cavern, visited):
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
                if (new_y >= 0 and new_y < max_y) and (new_x >= 0 and new_x < max_x)and (new_y, new_x) not in visited:
                        neighbors.append((new_y, new_x))

    return neighbors
def dijkstras(cavern, visited):
    #dijkstra's algo
    while len(entry_finder) > 0:
        # if len(entry_finder) % 100 == 0: #print out progress
        #     print(len(entry_finder))
        curr_pos, curr_risk = pop_task()
        neighbors = getNeighbors(curr_pos, cavern, visited)
        for neighbor in neighbors:
            tent_risk = curr_risk + cavern[neighbor[0]][neighbor[1]]
            entry = entry_finder[neighbor]
            if tent_risk < entry[0]:
                add_task(neighbor, tent_risk)
                prev_pos[neighbor] = curr_pos
        visited[curr_pos] = curr_risk
    return visited

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
    visited = create_pq(cavern, start)
    visited = dijkstras(cavern, visited)
    return visited[exit]


print(get_answer("input"))