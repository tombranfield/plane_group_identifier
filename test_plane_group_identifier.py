"""
Tests for plane_group_identifier.py
"""

from plane_group_identifier import *
import pytest


@pytest.mark.parametrize("correct_input", [1, 2, 3, 4, 6])
def test_is_valid_order_rotation_true(correct_input):
    assert is_valid_order_rotation(correct_input) == True


@pytest.mark.parametrize("invalid_input", [0, 5, 7, "string", None])
def test_is_valid_order_rotation_false(invalid_input):
    assert is_valid_order_rotation(invalid_input) == False


@pytest.mark.parametrize("valid_order", [1, 2, 3, 4, 6, 7])
def test_get_highest_order_rotation(monkeypatch, valid_order):
    monkeypatch.setattr("builtins.input", lambda _: valid_order)
    user_response = get_highest_order_rotation()
    assert user_response == valid_order



