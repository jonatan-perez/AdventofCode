import pytest
import day05_problem1
import day05_problem2

with open("2021/day05-hydrothermal-venture/test_input.txt") as f:
    instructions = []
    for line in f:
        split_line = line.split(" -> ")
        start = [int(num) for num in split_line[0].split(",")]
        end = [int(num) for num in split_line[1].split(",")]
        instructions.append([start, end])

def test_problem1():
    assert day05_problem1.calc_overlaps(instructions) == 5

def test_problem2():
    assert day05_problem2.calc_overlap(instructions) == 12