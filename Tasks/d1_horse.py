from math import factorial


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """

    rows, cols = shape[0], shape[1]
    end_row, end_col = point[0], point[1]

    board = [[0 for i in range(cols)] for j in range(rows)]
    board[0][0] = 1

    for r in range(rows):
        for c in range(cols):
            if r - 2 >= 0 and c - 1 >= 0:
                board[r][c] += 2 * board[r - 2][c - 1]
            if r - 2 >= 0 and c + 1 < cols:
                board[r][c] += 2 * board[r - 2][c + 1]
            if r - 1 >= 0 and c - 2 >= 0:
                board[r][c] += 2 * board[r - 1][c - 2]
            if r - 1 >= 0 and c + 2 < cols:
                board[r][c] += 2 * board[r - 1][c + 2]

    return board[end_row][end_col]






