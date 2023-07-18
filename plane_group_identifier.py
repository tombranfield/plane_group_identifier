"""
A script that identifies the plane group of a two-dimensional pattern given
user-supplied information.

Adapted from the flow chart in "The Basics of Crystallography and Diffraction",
chapter 2.

Usage: ./plane_group_identifier.py
"""

import sys
from typing import Union


class AnswerSequence:
    """
    A class representing the sequence of answers given by a user to
    identify the plane group of the pattern.
    """
    def __init__(self):
        self._sequence = sequence

    @property
    def sequence(self):
        """The sequence of answers represented as a string"""
        return self._radius

    def add(self, answer: Union[int, bool]):
        """Add an answer to the answer sequence"""
        if value.isinstance(answer, int):
            self._sequence += str(order_value)
        if value.instance(answer, bool):
            self._sequence += str(int(answer))


def is_valid_order_rotation(num: int) -> bool:
    """
    Tests whether a given input string is a valid order of rotation.
    """
    # Note this holds for plane groups. Quasicrystals not considered.
    if num in [1, 2, 3, 4, 6]:
        return True
    return False


def get_highest_order_rotation() -> int:
    """
    Prompts the user for the highest order of rotation present in the pattern,
    then returns it.
    """
    prompt_message = "What is the highest order of rotation of the pattern? "
    while True:
        user_response = input(prompt_message)
        check_if_quit_input(user_response)
        try:
            user_response = int(user_response)
        except ValueError:
            print("You must enter an integer 1, 2, 3, 4, or 6.")
        else:
            if is_valid_order_rotation(user_response):
                return user_response
            print("Only values 1, 2, 3, 4, and 6 are allowed.")


def check_if_quit_input(user_response):
    """
    Checks if the user wants to quit, and stops the program if they do.
    """
    # Potential entangement if we decide to change these
    # As will affects test suite (need to change in multiple places
    # Put constants at top?
    quit_strings = ["q", "quit", "exit"]
    try:
        user_response = user_response.lower()
    except AttributeError:
        pass
    else:
        if user_response in quit_strings:
            quit_program()


def yes_or_no_question(question: str) -> bool:
    """
    Prompts the user with a supplied question whose answer is yes or no, then
    returns True if yes and False if no.
    """
    prompt_message = question
    while True:
        user_response = input(prompt_message).lower()
        check_if_quit_input(user_response)
        if user_response in ["y", "yes"]:
            return True
        if user_response in ["n", "no"]:
            return False
        print("Invalid input.")


def is_reflection_present() -> bool:
    """
    Prompts the user whether reflection is present in the pattern then returns
    True if present and False if not.
    """
    prompt_message = "Is reflection present? (Y/n) "
    return yes_or_no_question(prompt_message)


def quit_program():
    """
    Prints a message that the program is stopping, then stops the
    program.
    """
    print("Program aborted.")
    sys.exit()


def convert_bool_to_str_1_or_0(in_bool) -> str:



def main():
    """Main program."""
    answer_sequence = AnswerSequence()

    highest_order_of_rotation = get_highest_order_rotation()
    answer_sequence.add_order_of_rotation(highest_order_of_rotation)

    reflection_present = is_reflection_present()
    answer_sequence += add_bool_answer_to_sequence(reflection_present)

    print(answer_sequence)


if __name__ == "__main__":
    main()
