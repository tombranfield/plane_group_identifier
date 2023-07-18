"""
Tests for plane_group_identifier.py
"""

from plane_group_identifier import *
import pytest


# Note these are copied as-is to the tests (not copied), so do not
# have code that mutates them as further tests will be affected.
VALID_ORDERS_OF_ROTATION = [1, 2, 3, 4, 6]
YES_PHRASES = ["y", "yes", "Y", "YES"]
NO_PHRASES = ["n", "no", "N", "NO"]


@pytest.mark.parametrize("correct_input", VALID_ORDERS_OF_ROTATION)
def test_is_valid_order_rotation_true(correct_input):
    assert is_valid_order_rotation(correct_input) == True


@pytest.mark.parametrize("invalid_input", [0, 5, 7, "string", None])
def test_is_valid_order_rotation_false(invalid_input):
    assert is_valid_order_rotation(invalid_input) == False


@pytest.mark.parametrize("valid_order", VALID_ORDERS_OF_ROTATION)
def test_get_highest_order_rotation(monkeypatch, valid_order):
    monkeypatch.setattr("builtins.input", lambda _: valid_order)
    user_response = get_highest_order_rotation()
    assert user_response == valid_order


@pytest.mark.parametrize("yes_input", YES_PHRASES)
def test_yes_or_no_question_true(monkeypatch, yes_input):
    monkeypatch.setattr("builtins.input", lambda _: yes_input)
    user_response = yes_or_no_question("Hi?")
    assert user_response == True


@pytest.mark.parametrize("no_input", NO_PHRASES)
def test_yes_or_no_question_false(monkeypatch, no_input):
    monkeypatch.setattr("builtins.input", lambda _: no_input)
    user_response = yes_or_no_question("Hi?")
    assert user_response == False


# def test_check_if_quit_input()
