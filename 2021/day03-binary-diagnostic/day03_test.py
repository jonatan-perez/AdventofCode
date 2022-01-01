import pytest
import problem1
import problem2

with open("2021/day03-binary-diagnostic/test_input.txt") as f:
    diag_report = [line.rstrip('\n') for line in f]

num_len = len(diag_report[0])

def test_problem1():
    assert problem1.calc_power_consumption(diag_report) == 198

def test_problem2():
    assert (problem2.calc_oxygen_rating(diag_report, num_len) * problem2.calc_co2_rating(diag_report, num_len)) == 230