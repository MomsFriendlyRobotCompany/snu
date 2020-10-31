from snu.snu import Vector
from snu.snu import Twist
from snu.snu import Wrench
from snu.snu import Quaternion
import numpy as np
import pytest


def test_vector():
    v = Vector(1.,2.,3.)
    # assert v.x == 1 and v.y == 2 and v.z == 3
    assert np.all([v, [1,2,3]])
    assert np.all([v.to_tuple(), [1,2,3]])
    assert isinstance(v.to_tuple(), tuple)
    assert v == v

    # with pytest.raises(Exception):
    #     if v != v:
    #         raise Exception()
    for i,val in enumerate([1,2,3]):
        assert v[i] == val

    vv = Vector(4,5,6)
    m = vv-v
    # assert m.x == 3 and m.y == 3 and m.z == 3
    assert np.all([m, [3,3,3]])

    m = v-vv
    # assert m.x == -3 and m.y == -3 and m.z == -3
    assert np.all([m, [-3,-3,-3]])

    m = .1*vv
    # assert np.all([m.to_tuple(), [.4,.5,.6]])
    assert np.all([m, [.4,.5,.6]])

    # assert vv.x == 4 and vv.y == 5 and vv.z == 6
    assert np.all([vv, [4,5,6]])

def test_twist():
    t = Twist()
    print(t)
    assert True

def test_quaternion():
    q = Quaternion()
    assert q.w == 1.0
