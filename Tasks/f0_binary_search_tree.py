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
        current_node, prev_node = self._find(key)
        if not current_node:
            return None

        if not prev_node:
            result = (self.root["key"], self.root["value"])
            self.root = self.remove_root()
            return result

        result = (current_node["key"], current_node["value"])
        self.delete_node(current_node, prev_node)

        return result

    def remove_root(self):
        current_node = self.root
        if not current_node["left"]:
            return current_node["right"]
        if not current_node["right"]:
            return current_node["left"]

        suc, prev = self.get_successor(current_node)
        current_node["value"] = suc["value"]
        self.delete_node(suc, prev)

        return current_node


    def delete_node(self, current_node, prev_node):
        if prev_node["left"] and prev_node["left"] == current_node:
            prev_node["left"] = self.del_node(current_node)
        else:
            prev_node["right"] = self.del_node(current_node)

    def del_node(self, current_node):
        if not current_node["left"] and not current_node["right"]:
            return None

        if not current_node["left"] or not current_node["right"]:
            if not current_node["left"]:
                child_node = current_node["right"]
                current_node["right"] = None
                return child_node
            else:
                child_node = current_node["left"]
                current_node["left"] = None
                return child_node

        successor, prev_successor = self.get_successor(current_node)
        current_node["value"] = successor["value"]
        self.delete_node(successor, prev_successor)
        return current_node

    def get_successor(self, current_node):
        prev = current_node
        suc = current_node["right"]

        while suc["left"] is not None:
            prev = suc
            suc = suc["left"]

        return suc, prev

    def find(self, key: int) -> Optional[Any]:

        current_node, _ = self._find(key)
        if current_node is not None:
            return current_node["value"]

    def _find(self, key):
        if not self.root:
            return None, None

        prev_node = None
        current_node = self.root
        while current_node["key"] is not None:
            if current_node["key"] == key:
                break

            prev_node = current_node
            if current_node["key"] < key:
                current_node = current_node["right"]
            else:
                current_node = current_node["left"]

            if not current_node:
                raise KeyError("Key not found")

        return current_node, prev_node

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        self.root = None
