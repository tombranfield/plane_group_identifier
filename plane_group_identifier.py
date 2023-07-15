"""
A script that identifies the plane group of a two-dimensional pattern given 
user-supplied information.

Adapted from the flow chart in "The Basics of Crystallography and Diffraction",
chapter 2.

Usage: ./identifying_plane_groups.py
"""

import sys


def is_valid_order_rotation(num: int) -> bool:
    """
    Tests whether a given input string is a valid order of rotation.
    """
    if num in [1, 2, 3, 4, 6]:
        return True
    return False


def get_highest_order_rotation() -> int:
    """
    Prompts the user for the highest order of rotation present in the pattern,]
    then returns it.
    """
    prompt_message = "What is the highest order of rotation of the pattern?"
    while True:
        user_response = input(prompt_message)
        if user_response in QUIT_STRINGS:
            quit_program()
        try:
            user_response = int(user_response)
        except ValueError:
            print("Invalid input. Please enter 1, 2, 3, 4, or 6.")
        else:
            if is_valid_order_rotation(user_response):
                return user_response


def check_if_quit_input(user_input):
    """
    Checks if the user wants to quit, and stops the program if they do.
    """
    quit_strings = ["q", "quit", "exit"]
    if user_response in quit_strings:
        quit_program()
        

def is_reflection_present(str) -> bool:
    """
    Prompts the user whether reflection is present in the pattern then returns
    the corresponding bool.
    """
    prompt_message = "Is reflection present? (Y/n)"
    while True:
        user_response = input(prompt_message).lower()
        if user_response in QUIT_STRINGS:
            quit_program()
        elif user_response in ["y", "yes"]:
            return True
        elif user_response in ["n", "no"]:
            return False
        else:
            print("Invalid input.")


def quit_program():
    """
    Prints a message that the program is stopping, then stops the
    program.
    """
    print("Program aborted.")
    sys.exit()


def main():
    """Main program."""
    highest_order_of_rotation = get_highest_order_rotation()
    reflection_present = is_reflection_present()
    print(highest_order_of_rotation, reflection_present)


if __name__ == "__main__":
    main()
