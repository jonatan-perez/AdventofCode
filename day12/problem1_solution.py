with open("input.txt") as f:
    valid_paths = {}
    path_pairs = [line.replace("\n", "") for line in f]

    for line in path_pairs:
        path = line.split("-")
        try:
             valid_paths[path[0]].append(path[1])
        except:
            valid_paths[path[0]] = [path[1]]
        try: 
            valid_paths[path[1]].append(path[0])
        except:
            valid_paths[path[1]] = [path[0]]


total_paths = 0


def find_all_paths(curr_cave, valid_paths, current_path):
    global total_paths

    if curr_cave == "end":
        total_paths += 1
        return 
    else: 
        for next_path in valid_paths[curr_cave]:
            if (next_path.islower() and next_path not in current_path) or next_path.islower() == False:
                current_path.append(curr_cave)
                find_all_paths(next_path, valid_paths, current_path)
                current_path.remove(curr_cave)

find_all_paths("start", valid_paths, [])
print(total_paths)