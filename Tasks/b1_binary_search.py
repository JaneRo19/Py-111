from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left_border = 0
    right_border = len(arr)

    while left_border < right_border:
        middle = (right_border + left_border) // 2

        if elem > arr[middle]:
            left_border = middle + 1
        else:
            right_border = middle

        if arr[left_border] == elem:
            return left_border




