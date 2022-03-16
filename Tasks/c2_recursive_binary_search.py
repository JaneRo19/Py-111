from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, left_border=None, right_border=None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    if left_border is None:
        left_border = 0
    if right_border is None:
        right_border = len(arr) - 1

    if left_border >= right_border:
        if arr[left_border] == elem:
            return left_border
        else:
            return None

    middle = (left_border + right_border) // 2

    if arr[middle] < elem:
        left_border = middle + 1
    else:
        right_border = middle

    return binary_search(elem, arr, left_border, right_border)
