"""
Tests for plane_group_identifier.py
"""

from plane_group_identifier import *
import pytest


YES_TEST_STRINGS = ["y", "yes", "Y", "YES"]
NO_TEST_STRINGS = ["n", "no", "N", "NO"]
QUIT_TEST_STRINGS = ["q", "quit", "exit", "Q", "QUIT", "EXIT"]


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


@pytest.mark.parametrize("yes_input", YES_TEST_STRINGS)
def test_yes_or_no_question_true(monkeypatch, yes_input):
    monkeypatch.setattr("builtins.input", lambda _: yes_input)
    user_response = yes_or_no_question("Hi?")
    assert user_response == True


@pytest.mark.parametrize("no_input", NO_TEST_STRINGS)
def test_yes_or_no_question_false(monkeypatch, no_input):
    monkeypatch.setattr("builtins.input", lambda _: no_input)
    user_response = yes_or_no_question("Hi?")
    assert user_response == False


@pytest.mark.parametrize("quit_input", QUIT_TEST_STRINGS)
def test_check_if_quit_input(monkeypatch, quit_input):
    monkeypatch.setattr("builtins.input", lambda _: quit_input)
    with pytest.raises(SystemExit):
        check_if_quit_input(quit_input)


@pytest.mark.parametrize("valid_int", VALID_ORDERS_OF_ROTATION)
def test_answer_sequence_add_valid_int(valid_int):
    answer_sequence = AnswerSequence()
    answer_sequence.add(valid_int)
    assert answer_sequence.string == str(valid_int)


@pytest.mark.parametrize("invalid_int", [-5, -1, 0, 5, 10])
def test_answer_sequence_add_invalid_int(invalid_int):
    answer_sequence = AnswerSequence()
    with pytest.raises(ValueError):
        answer_sequence.add(invalid_int)


def test_answer_sequence_add_bool_true():
    answer_sequence = AnswerSequence()
    answer_sequence.add(True)
    assert answer_sequence.string == "Y"


def test_answer_sequence_add_bool_false():
    answer_sequence = AnswerSequence()
    answer_sequence.add(False)
    assert answer_sequence.string == "N"


def test_answer_sequence_add_in_succession():
    answer_sequence = AnswerSequence()
    answer_sequence.add(4)
    answer_sequence.add(False)
    answer_sequence.add(True)
    assert answer_sequence.string == "4NY"


