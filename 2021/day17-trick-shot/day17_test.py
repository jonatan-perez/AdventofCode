import pytest
import day17_problem1
import day17_problem2

def test_problem1():
    assert day17_problem1.get_answer("test_input") == 45

def test_problem2():
    assert day17_problem2.get_answer("test_input") == 112