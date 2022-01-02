import pytest
import day08_problem1
import day08_problem2

with open("2021/day08-seven-segment-search/test_input.txt") as f:
    lines = [line.rstrip("\n").split(" | ") for line in f]
    outputs = [line[1].split(" ") for line in lines]


def test_problem1():
    assert day08_problem1.count_simple_digits(outputs) == 26

def test_problem2():
    input_code = day08_problem2.get_input_code(lines)
    assert day08_problem2.add_output_values(input_code, outputs) == 61229