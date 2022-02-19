"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    elem_min = arr[0]
    result = 0
    for index in range(len(arr)):
        if elem_min > arr[index]:
            elem_min = arr[index]
            result = index
    return result

