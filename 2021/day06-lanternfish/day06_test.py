import pytest
import day06_problem1
import day06_problem2

with open("2021/day06-lanternfish/test_input.txt") as f:
   lanternfish =  [int(i) for i in f.readline().strip("\n").split(",")]

def test_problem1():
    assert day06_problem1.processOneDay(lanternfish, 18) == 26
    assert day06_problem1.processOneDay(lanternfish, 80) == 5934

def test_problem2():
    lanternfish = day06_problem2.createLanternfishList("2021/day06-lanternfish/test_input.txt")
    assert day06_problem2.processOneDay(lanternfish, 256) == 26984457539

