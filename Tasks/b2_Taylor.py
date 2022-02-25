"""
Taylor series
"""
from typing import Union
from math import factorial
from itertools import count
EPSILON = 0.00001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    sum_ = 0
    top = 1
    bottom = 1
    for i in count(1, 1):
        current_item = top / bottom
        sum_ += current_item
        if abs(current_item) < EPSILON:
            return sum_
        top = top * x
        bottom = bottom * i


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """

    sum_ = 0
    top = x
    bottom = 1
    sign = 1
    for i in count(3, 2):
        current_item = sign * top / bottom
        sum_ += current_item
        if abs(current_item) < EPSILON:
            return sum_
        top = top * (x ** 2)
        bottom = bottom * i * (i - 1)
        sign = -sign
