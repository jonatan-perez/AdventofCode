from collections import Counter

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

find_all_paths("start", valid_paths, [])
print(total_paths)
