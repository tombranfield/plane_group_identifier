"""
A script that identifies the plane group of a two-dimensional pattern given
user-supplied information.

Adapted from the flow chart in "The Basics of Crystallography and Diffraction",
chapter 2, pg. 69, Third Edition, 2009.

Usage: ./plane_group_identifier.py
"""

import sys
from typing import Union


PLANE_GROUP_SEQUENCE = {
    "1YY":  "cm",
    "1YN":  "pm",
    "1NY":  "pg",
    "1NN":  "p1",
    "2YYY": "p2mm",
    "2YYN": "c2mm",
    "2YN":  "p2mg",
    "2NY":  "p2gg",
    "2NN":  "p2",
    "3YY":  "p3m1",
    "3YN":  "p3m1",
    "3N":   "p3",
    "4YY":  "p4mm",
    "4YN":  "p4gm",
    "4N":   "p4",
    "6Y":   "p6mm",
    "6N":   "p6",
}


SEQUENCE_QUESTIONS = {
    "1Y": "Is there glide-reflection in an axis which is not a reflection axis?",
    "1N": "Is glide-reflection present?",
    "2Y": "Do reflections occur in two directions?",
    "2YY": "Are all centres of rotation on reflection axes?",
    "2N": "Is glide-reflection present?",
    "3Y": "Are all centres of rotation on reflection axes?",
    "4Y": "Do reflections occur in axes which intersect at 45\u00B0?",
}


VALID_ORDERS_OF_ROTATION = [1, 2, 3, 4, 6]


class AnswerSequence:
    """
    A class representing the sequence of answers given by a user to
    identify the plane group of the pattern.
    """
    def __init__(self):
        self._sequence = ""

    @property
    def sequence(self) -> str:
        """The sequence of answers represented as a string"""
        return self._sequence

    def add(self, answer: Union[int, bool]):
        """Adds the supplied answer to the answer sequence"""
        if isinstance(answer, bool):
            return_char = "Y" if answer else "N"
            self._sequence += return_char
        elif isinstance(answer, int):
            self._sequence += str(answer)
        else:
            raise TypeError("Unsupported type for this operation")


def is_valid_order_rotation(num: int) -> bool:
    """
    Tests whether a given input string is a valid order of rotation.
    """
    # Note this holds for plane groups. Quasicrystals not considered.
    if num in VALID_ORDERS_OF_ROTATION:
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


def main():
    """Main program."""
    answer_sequence = AnswerSequence()

    answer_sequence.add(get_highest_order_rotation())
    answer_sequence.add(is_reflection_present())


if __name__ == "__main__":
    main()
