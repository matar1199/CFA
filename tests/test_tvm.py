import pytest

from exercises.tvm import future_value, npv, present_value


def test_future_value():
    assert future_value(1000, 0.05, 10) == pytest.approx(1628.89, abs=0.01)


def test_present_value_is_inverse_of_future_value():
    assert present_value(future_value(500, 0.07, 3), 0.07, 3) == pytest.approx(500)


def test_npv():
    assert npv(0.10, [-100, 110]) == pytest.approx(0)
