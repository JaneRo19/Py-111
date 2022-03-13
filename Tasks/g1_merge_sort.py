from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    n = len(container)
    if n < 2:
        return container

    left = sort(container[:n // 2])
    right = sort(container[n // 2:])
    i = j = 0
    res_container = []

    while i < len(left) or j < len(right):
        if not i < len(left):
            res_container.append(right[j])
            j += 1
        elif not j < len(right):
            res_container.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res_container.append(left[i])
            i += 1
        else:
            res_container.append(right[j])
            j += 1

    return res_container
