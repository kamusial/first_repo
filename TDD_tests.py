#import functions
from functions import *
import pytest

#print(functions.multiply(5, 6))
#print(multiply(5, 6))
#
# def test_multiply():
#     assert multiply(5, 10) == 50
#     assert multiply(100, 1.1) == 110
#     assert multiply(1.5, 1.5) == 2.25
#     assert multiply(0.0000001, 100) == 0.00001
#     assert multiply('mama', 3) == 'mamamamamama'
#     assert multiply(None, 5) == None
#
# def test_number_of_letters():
#     assert no_of_letter('mama') == 4
#     assert no_of_letter('mama.tata') == 8
#     #nie odpowiedzieliśmy na ten warunek)

@pytest.mark.parametrize('number, result', [(1, 1), (3, 'fiss')])

def test_fissbuzz_param(number, result):
    assert fissbuzz(number) == result

def test_fissbuzz_basic():
    assert fissbuzz(1) == 1
    assert fissbuzz(2) == 2
    assert fissbuzz(3) == 'fiss'
    assert fissbuzz(4) == 4
    assert fissbuzz(6) == 'fiss'
    assert fissbuzz(5) == 'buzz'
    assert fissbuzz(10) == 'buzz'
    assert fissbuzz(15) == 'fissbuzz'

def test_fissbuzz_advanced():
    assert fissbuzz(1.3) == 1
    assert fissbuzz(1.9) == 1
    assert fissbuzz('1') == 1
    assert fissbuzz('1.7') == 1
    assert fissbuzz(5.9) == 'buzz'
    assert fissbuzz('5.99') == 'buzz'
    assert fissbuzz(0) == None
    assert fissbuzz(0.999) == None
    assert fissbuzz('mama') == None
    assert fissbuzz(-5) == None
    assert fissbuzz('-15.8') == None


