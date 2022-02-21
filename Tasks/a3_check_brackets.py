def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    stack = []
    is_good = True
    for bracket in brackets_row:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if not stack:
                is_good = False
                break
            open_bracket = stack.pop()
            if open_bracket == "(" and ")":
                continue
            is_good = False
    if is_good and len(stack) == 0:
        return True
    else:
        return False

