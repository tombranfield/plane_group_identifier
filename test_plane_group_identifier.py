"""
Tests for plane_group_identifier.py
"""

from plane_group_identifier import *
import pytest


# This will hold a dictionary with key-value pairs corresponding
# to the input and the output plane groups
@pytest.fixture
def correct_results():
    return {}





@pytest.mark.parametrize("correct_input", [1, 2, 3, 4, 6])
def test_is_valid_order_rotation_true(correct_input):
    assert is_valid_order_rotation(correct_input) == True


@pytest.mark.parametrize("invalid_input", [0, 5, 7, "string", None])
def test_is_valid_order_rotation_false(invalid_input):
    assert is_valid_order_rotation(invalid_input) == False



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
# Need to learn about fixtures, mocking, and monkeypatch
def test_get_highest_order_rotation():
    assert (1, 2, 3) == (1, 2, 3)


