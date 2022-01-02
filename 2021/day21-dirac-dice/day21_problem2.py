with open("2021/day21-dirac-dice/input.txt") as f:
    p1_pos = int(f.readline().rstrip("\n")[-1])
    p2_pos = int(f.readline().rstrip("\n")[-1])

CACHE = {}
def diracGame(p1_score, p1_pos, p2_score, p2_pos):
    if p1_score >= 21:
        print("here")
        return (1, 0)
    elif p2_score >= 21:
        return (0, 1)
    elif (p1_score, p1_pos, p2_score, p2_pos) in CACHE:
        return CACHE[(p1_score, p1_pos, p2_score, p2_pos)]

    else:
        score = (0, 0)
        for d1 in [1, 2, 3]:
            for d2 in [1, 2, 3]:
                for d3 in [1, 2, 3]:
                    new_pos = p1_pos + (d1 + d2 + d3)
                    if new_pos > 10:
                        new_pos = new_pos % 10
                    new_score = p1_score + new_pos

                    #print(p2_score, p2_pos, new_score, new_pos)
                    p1, p2 = diracGame(p2_score, p2_pos, new_score, new_pos)
                    score = (score[0] + p2, score[1] + p1)

        CACHE[(p1_score, p1_pos, p2_score, p2_pos)] = score
        return score

print(max(diracGame(0, p1_pos, 0, p2_pos)))
