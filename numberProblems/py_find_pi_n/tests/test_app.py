from src.py_find_pi_n.find_pi import find_pi

def test_find_pi():
    result = find_pi(5)
    assert isinstance(result, str)

def test_find_pi_digits():
    assert find_pi(3) == '3.141'
    assert find_pi(6) == '3.141592'
    assert find_pi(99) == "Error too many digits; enter 50 or less!"