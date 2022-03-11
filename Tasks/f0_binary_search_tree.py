"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx


class BinarySearchTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def create_node(key, value, left=None, right=None):
        return {
            "key": key,
            "value": value,
            "left": left,
            "right": right
        }

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """

        if self.root is None:
            self.root = self.create_node(key, value)
        else:
            current_node = self.root
            current_key = current_node["key"]

            while True:
                if key > current_key:
                    if current_node["right"] is None:
                        current_node["right"] = self.create_node(key, value)
                        break
                    else:
                        current_node = current_node["right"]
                else:
                    if current_node["left"] is None:
                        current_node["left"] = self.create_node(key, value)
                        break
                    else:
                        current_node = current_node["left"]

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        print(key)
        return None

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        return None
