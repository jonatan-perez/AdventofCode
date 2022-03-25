from collections import Counter

total_paths = 0

def find_all_paths(curr_cave, valid_paths, current_path):
    global total_paths

    if curr_cave == "end":
        total_paths += 1
        return 
    else: 
        for next_path in valid_paths[curr_cave]:
            if next_path.islower() and next_path != "start":
                small_cave_count = Counter(current_path).most_common()
                if next_path not in current_path:
                    current_path.append(next_path) #need to add next_path otherwise recursive loop
                    find_all_paths(next_path, valid_paths, current_path)
                    current_path.remove(next_path)
                elif next_path in current_path and small_cave_count[0][1] < 2:
                    current_path.append(next_path)
                    find_all_paths(next_path, valid_paths, current_path)
                    current_path.remove(next_path)
            elif next_path.islower() == False: #not lowercase cave can visit as many times as necessary
                find_all_paths(next_path, valid_paths, current_path)
    return total_paths

def get_answer(file):
    #reset global variable each time you solve for new input
    #not easy to get rid of global variable with recursive solution
    global total_paths
    total_paths = 0
    
    with open(f"2021/day12-passage-pathing/{file}.txt") as f:
        valid_paths = {}
        path_pairs = [line.replace("\n", "") for line in f]

        for line in path_pairs:
            path = line.split("-")
            #check if path key, value pair exists otherwise create it
            try:
                valid_paths[path[0]].append(path[1])
            except:
                valid_paths[path[0]] = [path[1]]
            try: 
                valid_paths[path[1]].append(path[0])
            except:
                valid_paths[path[1]] = [path[0]]

    answer = find_all_paths("start", valid_paths, [])

    return answer