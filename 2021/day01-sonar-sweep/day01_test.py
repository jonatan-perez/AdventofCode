import pytest
import problem1
import problem2

numbers = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def test_problem1():
    assert problem1.count_increases(numbers) == 7

def test_problem2():
    assert problem2.larger_sums(numbers) == 5


