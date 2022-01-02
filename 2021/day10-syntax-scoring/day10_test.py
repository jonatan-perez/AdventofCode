import pytest
import day10_problem1
import day10_problem2

def test_problem1():
    assert day10_problem1.calc_total("test_input") == 26397

def test_problem2():
    assert day10_problem2.get_middle_score("test_input") == 288957