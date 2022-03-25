import pytest
import day11_problem1
import day11_problem2

def test_problem1():
    assert day11_problem1.get_answer("test_input", 10) == 204
    assert day11_problem1.get_answer("test_input", 100) == 1656

def test_problem2():
    assert day11_problem2.get_answer("test_input") == 195