"""
Tests for plane_group_identifier.py
"""

from plane_group_identifier import *
import pytest


# TODO put valid orders of rotation into a list in a fixture

@pytest.mark.parametrize("correct_input", [1, 2, 3, 4, 6])
def test_is_valid_order_rotation_true(correct_input):
    assert is_valid_order_rotation(correct_input) == True


@pytest.mark.parametrize("invalid_input", [0, 5, 7, "string", None])
def test_is_valid_order_rotation_false(invalid_input):
    assert is_valid_order_rotation(invalid_input) == False


@pytest.mark.parametrize("valid_order", [1, 2, 3, 4, 6])
def test_get_highest_order_rotation(monkeypatch, valid_order):
    monkeypatch.setattr("builtins.input", lambda _: valid_order)
    user_response = get_highest_order_rotation()
    assert user_response == valid_order


@pytest.mark.parametrize("yes_input", ["y", "yes", "Y", "YES"])
def test_yes_or_no_question_true(monkeypatch, yes_input):
    monkeypatch.setattr("builtins.input", lambda _: yes_input)
    user_response = yes_or_no_question("Hi?")
    assert user_response == True


# def test_check_if_quit_input()
