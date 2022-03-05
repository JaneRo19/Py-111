from math import factorial

def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """

    rows = shape[0]
    cols = shape[1]
    count = 2
    sum_ = 0
    list_ = []

    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            # if (i == 0 and j == 0) or (not 0 <= i <= rows) or (not 0 <= j <= cols):
            #     return 0
            # if i == 0 and j == 0:
            #     return 1
            #
            # if not 0 <= i < rows:
            #     return 0
            #
            # if not 0 <= j < cols:
            #     return 0

            if (list_[i - 2][j + 1]) or (list_[i - 1][j + 2]) or (list_[i - 1][j - 2]) or (list_[i - 2][j - 1]):
                count += 2 * i
                list_.append(count)

    return list_[-1]

