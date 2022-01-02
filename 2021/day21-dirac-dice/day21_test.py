import pytest
import day21_problem1
import day21_problem2

with open("2021/day21-dirac-dice/test_input.txt") as f:
    p1_pos = int(f.readline().rstrip("\n")[-1])
    p2_pos = int(f.readline().rstrip("\n")[-1])

def test_problem1():
    assert day21_problem1.get_losing_player_score(p1_pos, p2_pos) == 739785

def test_problem2():
    assert max(day21_problem2.diracGame(0, p1_pos, 0, p2_pos)) == 444356092776315