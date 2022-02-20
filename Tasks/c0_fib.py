def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError("n должно быть больше 0")

    else:
        if n in (1, 2):
            return 1

        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    fib_1 = 1
    fib_2 = 1

    if n < 0:
        raise ValueError("n не может быть меньше нуля")
    else:
        for _ in range(2, n):
            fib_1, fib_2 = fib_2, fib_1 + fib_2

    return fib_2
