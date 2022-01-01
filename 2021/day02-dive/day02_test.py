import pytest
import day02_problem1
import day02_problem2

with open("2021/day02-dive/test_input.txt") as f:
    input = [line.split() for line in f]

def test_problem1():
    assert day02_problem1.calc_pos(input) == 150

def test_problem2():
    assert day02_problem2.calc_pos(input) == 900