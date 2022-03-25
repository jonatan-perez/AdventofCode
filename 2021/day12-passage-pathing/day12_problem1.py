total_paths = 0

def find_all_paths(curr_cave, valid_paths, current_path):
    global total_paths

    if curr_cave == "end":
        total_paths += 1
    else: 
        for next_path in valid_paths[curr_cave]:
            if (next_path.islower() and next_path not in current_path) or next_path.islower() == False:
                current_path.append(curr_cave)
                find_all_paths(next_path, valid_paths, current_path)
                current_path.remove(curr_cave)
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