from main import Monomial
import pytest
lst = []
with open('tests.txt', 'r') as file:
    for line in file.readlines():
        line = line.split(' ')
        line = (line[0], line[1].replace('\n', ''))
        lst.append(line)


@pytest.mark.parametrize('monomial, result', lst)
def test_diff(monomial, result):
    assert Monomial.differentiate(Monomial(monomial)) == result
