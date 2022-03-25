import pytest
import day12_problem1
import day12_problem2

def test_problem1():
    assert day12_problem1.get_answer("test_input") == 10
    assert day12_problem1.get_answer("test_input2") == 19
    assert day12_problem1.get_answer("test_input3") == 226



def test_problem2():
    assert day12_problem2.get_answer("test_input") == 36
    assert day12_problem2.get_answer("test_input2") == 103
    assert day12_problem2.get_answer("test_input3") == 3509