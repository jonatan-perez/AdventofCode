import pytest
import day04_problem1
import day04_problem2

def test_problem1():
    assert day04_problem1.get_answer("test_input") == 4512

def test_problem2():
    assert day04_problem2.get_answer("test_input") == 1924