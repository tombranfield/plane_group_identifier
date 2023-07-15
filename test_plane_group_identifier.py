"""
Tests for plane_group_identifier.py
"""

from plane_group_identifier import *
import pytest


@pytest.mark.parametrize("in_num", [1, 2, 3, 4, 6])
def test_is_valid_order_rotation_true(in_num):
    assert is_valid_order_rotation(in_num) == True


@pytest.mark.parametrize("in_num", [0, 5, 7, "string", None])
def test_is_valid_order_rotation_false(in_num):
    assert is_valid_order_rotation(in_num) == False


def test_get_highest_order_rotation():
    assert (1, 2, 3) == (1, 2, 3)


