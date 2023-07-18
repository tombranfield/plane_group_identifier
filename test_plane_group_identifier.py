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


# Show user inputting [1, 2, 3, 4, 6] outputs that integer
def test_get_highest_order_rotation(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 1)
    user_response = get_highest_order_rotation()
    assert user_response == 1



