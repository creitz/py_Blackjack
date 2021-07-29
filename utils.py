
def get_integer_input(blurb: str, prompt: str):
    """
    Prompts the user to enter a bet amount as an integer, and returns the amount
    once an integer is input.

    Args:
        blurb (str): The string printed before input
        prompt (str): The string printed on the same line as the input

    Returns:
        [int]: The integer the user input
    """
    input_amt = None
    print(blurb)
    while input_amt is None or not input_amt.isnumeric():
        input_amt = input(prompt)

    return int(input_amt)
