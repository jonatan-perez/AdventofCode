import pytest
import problem02_1
import problem02_2

with open("2021/day02-dive/test_input.txt") as f:
    input = [line.split() for line in f]

def test_problem1():
    assert problem02_1.calc_pos(input) == 150

def test_problem2():
    assert problem02_2.calc_pos(input) == 900