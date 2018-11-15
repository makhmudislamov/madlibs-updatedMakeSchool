from time import sleep
import sys

# Inspiried by Asim and Ikey
# delaying print - effect


def delay_print(string):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)
    print('')
    return ">>"



# assigning yellow color to display output
yellow = "\033[33m"


def hpotter_theme():

        # Intro
    welcome_text = """Thank you for entering Hogwarts automagic portal!\n Harry is inviting you to his wedding but we wanna keep out messages from Dementors.\n 
    Please answer the following secret questions."""
    delay_print(yellow + welcome_text.upper())
    sleep(1)

    # Questions
    name = input(delay_print(
        yellow + "What is your name in Muggle world? "))
    sleep(1)
    delay_print(
        yellow + " Muggle names are funny. Sorting Hat will give you new name soon.")
    sleep(1)
    restaurant = input(delay_print("Which restaurant is your favorite? "))
    sleep(1)
    color = input(delay_print("Type the first color came to your mind "))
    sleep(1)
    animal = input(delay_print("Which animal scares you the most? "))
    sleep(1)
    car = input(delay_print("Your dream car "))
    sleep(1)
    street = input(delay_print("Type the street name that you live "))
    sleep(1)

    # Final text
    print(yellow + "Expecto Patronum !!! Chasing Dementors").upper()
    sleep(1)
    delay_print(yellow + "Hedwig is flying with you letter...")
    sleep(1)
    print(yellow + "Here is the message from Harry Potter:")

    delay_print(yellow + "I salute you " + yellow + name + "! " + yellow +
                "You cheated muggles and enrolled to Make School to join other tech wizards. Volendemort announced a reward for your GitHub authentication keys. "
                "The Wisley twins are waiting for your at " + yellow + restaurant +
                yellow + ". They will give u the Cloak of Invisibility, use it. Stay awake and look for "
                + yellow + color + " " + animal + yellow + ".\n It will lead you to Trinity. She will be in " + yellow + color + " " + car + yellow + " at " + yellow + street + yellow + ".\n End of line...")

    exit()

    # delay_print(yellow + "SEARCHING...")
    # sleep(2)
    # delay_print(yellow + "I see you are awake!")
    # sleep(1)
    # delay_print(yellow + "The Matrix has you now...")
    # sleep(1)
    # welcome_text = 'Welcome to the Matrix stranger! I know you have questions and I have answers for them. Ill dive into your subconcious\n for the answers you need. But before I have have to know you better'
    # delay_print(yellow + welcome_text.upper())
    # sleep(1)

""" 
Intro text:
Thank you for entering Hogwarts automagic portal. Harry is inviting you to his wedding but we wanna keep out messages from Dementors. 
Please answer the following secret questions.
"""
