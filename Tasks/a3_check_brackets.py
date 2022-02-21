def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    counter = 0
    for i in range(len(brackets_row)):
        if brackets_row[i] == "(" and brackets_row[0] != ")":
            counter += 1
        else:
            counter -= 1
    return True if counter == 0 else False

