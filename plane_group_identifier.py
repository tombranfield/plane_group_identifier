"""
Identifies a plane group of a two-dimensional pattern given
user-supplied information.

Usage:
    ./identifying_plane_groups.py
"""

import sys


QUIT_STRINGS = ["q", "quit", "exit"]


def quit_program(self):
    print("Program aborted.")
    sys.exit()


def get_highest_order_rotation(self):
    """
    Prompts the user for the highest order of rotation present
    in the pattern.
    """
    prompt_message = "What is the highest order of rotation of the pattern?"
    while True:
        user_input = input(prompt_message)
        if user_input in QUIT_STRINGS:
            quit_program()
        if is_valid_order_rotation(input):
            return user_input
        else:
            print("Invalid input. Please enter None, 2, 3, 4, or 6.")
        

    def is_valid_order_rotation(self):
        """
        Tests whether a given input is a valid order of rotation.
        """
        pass
