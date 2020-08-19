from mymath.arith import *
def test_add():
    assert add(1, 1) == 2

def test_subtract():
    assert subtract(2, 1) == -1

def test_double():
    assert double(3) == 6
    
def test_disp():
    d = displacement2([1, 1], [0, 0])
    assert d[0] == 1
    assert d[1] == 1
   
