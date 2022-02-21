"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from collections import defaultdict


class PriorityQueue:
    def __init__(self):
        self._priority_queue = defaultdict(list)

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        for key in self._priority_queue:
            if key == priority:
                self._priority_queue[key].append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if self._priority_queue:
            return self._priority_queue.pop(0)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        for key, value in self._priority_queue.items():
            if key == priority:
                if ind < len(self._priority_queue[key]):
                    return self._priority_queue[key][ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self._priority_queue.clear()
