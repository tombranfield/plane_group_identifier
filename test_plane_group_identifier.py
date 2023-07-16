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



# Testing get_highest_order_rotation() function
# It get input from the user
# It returns an integer
# So we need to mock user input
# Check correct user input gives correct output [1, 2, 3, 4, 6]
# So how to mock user input?
# Let's do lots of reading on pytest
# In fact, I'll setup a sandbox for learning it
# Copy lots of examples etc
# So leave this coding for a bit...
def test_get_highest_order_rotation():
    assert (1, 2, 3) == (1, 2, 3)


