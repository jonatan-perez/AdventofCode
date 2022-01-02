from collections import Counter

def get_inputs(file):
    with open(f"2021/day14-extended-polymerization/{file}.txt") as f:
        lines =  [line.strip("\n") for line in f]
        polymer = lines[0]
        instructions = [rule.split(" -> ") for rule in lines[2:]]
    
    rules = {}
    for instruction in instructions:
        rules[instruction[0]] = instruction[1]


    polymer_dic = Counter()
    for i in range(len(polymer) - 1):
        curr_polymer = polymer[i:i+2]
        polymer_dic[curr_polymer] += 1

    return polymer, rules, polymer_dic

def processStep(polymer_dic, days, rules):
    if days == 0:
        return polymer_dic
    else: 
        next_counts = Counter()
        keys = list(polymer_dic.keys())
        for pair in keys:
            val = polymer_dic[pair]
            left = pair[0]
            right = pair[1]
            ins = rules[pair]
            new_pair1 = left + ins
            new_pair2 = ins + right
            next_counts[new_pair1] += val
            next_counts[new_pair2] += val

        return processStep(next_counts, days - 1, rules)

def countSingleLetters(polymer_dic, polymer):
    keys = list(polymer_dic.keys())
    letter_count = Counter()

    for pair in keys:
        val = polymer_dic[pair]
        right = pair[1] #left is overcounted so only add right letter of pairs
        letter_count[right] += val

    letter_count[polymer[0]] += 1 #edge case first letter in original polymer excluded from for loop

    return letter_count

def get_answer(file, days):
    polymer, rules, polymer_dic = get_inputs(file)
    letter_count = countSingleLetters(processStep(polymer_dic, days, rules), polymer)
    return letter_count.most_common(1)[0][1] - letter_count.most_common()[-1][1]

print(get_answer("input", 40))
