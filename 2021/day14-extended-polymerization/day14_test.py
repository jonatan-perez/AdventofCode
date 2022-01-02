import pytest
import day14_problem1
import day14_problem2

def test_problem1():
    polymer, rules = day14_problem1.get_inputs("test_input")
    assert len(day14_problem1.processStep(polymer, 5, rules)) == 97
    assert len(day14_problem1.processStep(polymer, 10, rules)) == 3073
    assert day14_problem1.get_code("test_input", 10) == 1588

def test_problem2():
    assert day14_problem2.get_answer("test_input", 40) == 2188189693529