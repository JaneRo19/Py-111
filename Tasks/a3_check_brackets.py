def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    counter = 0
    for bracket in brackets_row:
        if bracket == "(":
            counter += 1
        else:
            counter -= 1
        if counter < 0:
            return False
    return counter == 0

