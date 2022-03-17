from math import factorial


def get_steps(r, c, rows, cols, board):
    while r < rows and c >= 0:
        if r - 2 >= 0 and c - 1 >= 0:
            board[r][c] += board[r - 2][c - 1]
        if r - 2 >= 0 and c + 1 < cols:
            board[r][c] += board[r - 2][c + 1]
        if r - 1 >= 0 and c - 2 >= 0:
            board[r][c] += board[r - 1][c - 2]
        if r + 1 < rows and c - 2 >= 0:
            board[r][c] += board[r + 1][c - 2]

        r += 1
        c -= 1


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

    for i in range(1, cols):
        get_steps(0, i, rows, cols, board)

    for i in range(1, rows):
        get_steps(i, cols - 1, rows, cols, board)

    return board[end_row][end_col]
#
#
    # rows = shape[0]
    # cols = shape[1]
    #
    # def get_steps(i, j):
    #     if i == 0 and j == 0:
    #         return 1
    #     if not 0 <= i < rows:
    #         return 0
    #     if not 0 <= j < cols:
    #         return 0
    #
    #     return sum([
    #         get_steps(i - 2, j + 1),
    #         get_steps(i - 2, j - 1),
    #         get_steps(i - 1, j - 2),
    #         get_steps(i + 1, j - 2)
    #     ])
    # return get_steps(point[0], point[1])


if __name__ == '__main__':
    assert 13309 == calculate_paths((7, 15), (6, 14))
    assert 2 == calculate_paths((4, 4), (3, 3))




