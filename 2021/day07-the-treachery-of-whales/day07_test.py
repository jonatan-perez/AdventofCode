import pytest
import day07_problem1
import day07_problem2

with open("2021/day07-the-treachery-of-whales/test_input.txt") as f:
    crab_positions = [int(x) for x in f.readline().rstrip('\n').split(",")]

def test_problem1():
    assert day07_problem1.calc_least_fuel(crab_positions) == 37

def test_problem2():
    assert day07_problem2.calc_least_fuel(crab_positions) == 168