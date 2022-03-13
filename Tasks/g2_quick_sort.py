from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) > 1:
        pivot = container.pop()
        left_lst, middle_lst, right_lst = [], [pivot], []
        for item in container:
            if item == pivot:
                middle_lst.append(item)
            elif item > pivot:
                right_lst.append(item)
            else:
                left_lst.append(item)
        return sort(left_lst) + middle_lst + sort(right_lst)
    else:
        return container

