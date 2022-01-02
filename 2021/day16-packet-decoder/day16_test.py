import pytest
import day16_problem1
import day16_problem2

def test_problem1():
    assert day16_problem1.get_answer("8A004A801A8002F478") == 16
    assert day16_problem1.get_answer("620080001611562C8802118E34") == 12
    assert day16_problem1.get_answer("C0015000016115A2E0802F182340") == 23
    assert day16_problem1.get_answer("A0016C880162017C3686B18A3D4780") == 31

def test_problem2():
    assert day16_problem2.get_answer("C200B40A82") == 3
    assert day16_problem2.get_answer("04005AC33890") == 54
    assert day16_problem2.get_answer("880086C3E88112") == 7
    assert day16_problem2.get_answer("CE00C43D881120") == 9
    assert day16_problem2.get_answer("D8005AC2A8F0") == 1
    assert day16_problem2.get_answer("F600BC2D8F") == 0
    assert day16_problem2.get_answer("9C005AC2F8F0") == 0
    assert day16_problem2.get_answer("9C0141080250320F1802104A08") == 1

