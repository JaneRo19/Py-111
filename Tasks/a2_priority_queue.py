"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.n = 11
        self.priority_queue = {x: [] for x in range(self.n)}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """

        self.priority_queue[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """

        for key, value in self.priority_queue.items():
            if len(value) != 0:
                return value.pop(0)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        if ind < len(self.priority_queue[priority]):
            return self.priority_queue[priority][ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        for key, value in self.priority_queue.items():
            value.clear()
