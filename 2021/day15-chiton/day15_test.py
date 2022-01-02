import pytest
import day15_problem1
import day15_problem2

def test_problem1():
    assert day15_problem1.get_answer("test_input") == 40

def test_problem2():
    assert day15_problem2.get_answer("test_input") == 315