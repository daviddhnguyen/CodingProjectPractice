from src.codingprojectpractice.find_pi import find_pi
from src.codingprojectpractice.find_e import find_e

def test_find_pi():
    result = find_pi(5)
    assert isinstance(result, str)

def test_pi_digits():
    assert find_pi(3) == '3.141'
    assert find_pi(6) == '3.141592'

def test_pi_error_msg():
    assert find_pi(99) == "Error too many digits; enter 50 or less!"

def test_find_e():
    result = find_e(3)
    assert isinstance(result, str)

def test_e_digits():
    assert find_e(3) == '2.718'
    assert find_e(10) == '2.7182818284'

def test_e_error_msg():
    assert find_e(99) == "Error too many digits; enter 50 or less!"