with open("test_input.txt") as f:
    p1_pos = int(f.readline().rstrip("\n")[-1])
    p2_pos = int(f.readline().rstrip("\n")[-1])

p1_score = 0
p2_score = 0

p1_turn = True
dice_rolls = 0
start_roll = 1

while p1_score < 1000 and p2_score < 1000:
    #print(roll)
    dice_rolls += 3
    if start_roll == 99:
        first_roll = 99
        second_roll = 100
        third_roll = 1
        start_roll = 2
    elif start_roll == 100:
        first_roll = 100
        second_roll = 1
        third_roll = 2
        start_roll = 3
    else:
        first_roll = start_roll
        second_roll = start_roll + 1
        third_roll = start_roll + 2
        start_roll = third_roll + 1
    
    total = first_roll + second_roll + third_roll

    if p1_turn:
        p1_pos += total
        if p1_pos > 10:
            p1_pos = p1_pos % 10
            if p1_pos == 0:
                p1_pos = 10
        p1_score += p1_pos
        p1_turn = False

    elif p1_turn == False: 
        p2_pos += total
        if p2_pos > 10:
            p2_pos = p2_pos % 10
            if p2_pos == 0:
                p2_pos = 10
        p2_score += p2_pos
        p1_turn = True

    if p1_score >= 1000 or p2_score >= 1000:
        losing_player = min([p1_score, p2_score])
        print("answer: ", losing_player * dice_rolls)
        break
