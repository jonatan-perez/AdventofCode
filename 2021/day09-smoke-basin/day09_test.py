import pytest
import day09_problem1
import day09_problem2

with open("2021/day09-smoke-basin/test_input.txt") as f:
    lines = [line.rstrip("\n") for line in f]
    vents = [[int(num) for num in line] for line in lines]

def test_problem1():
    assert day09_problem1.calc_risk_level(vents) == 15

def test_problem2():
    low_points = day09_problem2.get_low_points(vents)
    assert day09_problem2.get_largest_basins(low_points, vents) == 1134