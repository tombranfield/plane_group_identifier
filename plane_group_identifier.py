"""
A script that identifies a plane group of a two-dimensional pattern given 
user-supplied information.

Adapted from the flow chart in "The Basics of Crystallography and Diffraction",
chapter 2.

Usage: ./identifying_plane_groups.py
"""

import sys


QUIT_STRINGS = ["q", "quit", "exit"]


def is_valid_order_rotation(num: int) -> bool:
    """
    Tests whether a given input string is a valid order of rotation.
    """
    # Note "none" is a user-supplied answer to whether the pattern has
    # rotational symmetry or not. It is not to do with NoneType.
    if num in [1, 2, 3, 4, 6]:
        return True
    return False


def get_highest_order_rotation():
    """
    Prompts the user for the highest order of rotation present in the pattern,]
    then returns it.
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
        

def is_reflection_present(self) -> bool:
    """
    Prompts the user whether reflection is present in the pattern then returns
    the corresponding bool.
    """
    pass


def quit_program(self):
    print("Program aborted.")
    sys.exit()


def main():
    """Main program."""
    highest_order_of_rotation = get_highest_order_of_rotation()
    reflection_present = is_reflection_present()


if __name__ == "__main__":
    main()
