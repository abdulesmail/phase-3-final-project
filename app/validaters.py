def validate_choice(choice, quit_choice):
    """
    Choice should be an integer
    """
    if choice.isnumeric():
        return choice
    else:
        print("Provided wrong choice!!! Please choose correctly.")
        return quit_choice