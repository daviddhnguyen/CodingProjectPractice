from src.codingprojectpractice.find_e import find_e

def test_find_e():
    result = find_e(3)
    assert isinstance(result, str)

def test_e_digits():
    assert find_e(3) == '2.718'
    assert find_e(10) == '2.7182818284'

def test_e_error_msg():
    assert find_e(99) == "Error too many digits; enter 50 or less!"