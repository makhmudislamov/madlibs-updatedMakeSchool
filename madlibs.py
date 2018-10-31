from matrix import matrix_theme
# from hpotter import hpotter_theme

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def start_madlibs():

    theme_choice = user_input("choose M or H")
    if theme_choice in ["M", "m"]:
        matrix_theme()
    # elif theme_choice in ["H","h"]:
    #     hpotter_theme()
    # else:
    #     print("invalid input")

start_madlibs()
