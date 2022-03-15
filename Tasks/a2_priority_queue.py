"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priority_queue = {x: [] for x in range(11)}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        for key, value in self.priority_queue.items():
            if key == priority:
                value.append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if self.priority_queue:
            for key, value in self.priority_queue.items():
                if len(value) != 0:
                    return value.pop(0)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        for key, value in self.priority_queue.items():
            if key == priority:
                if ind < len(value):
                    return value[ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        for key, value in self.priority_queue.items():
            value.clear()
