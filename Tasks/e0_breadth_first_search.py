from typing import Hashable, List
import networkx as nx
from collections import deque


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    path_nodes = []
    wait_nodes = deque()
    visited_nodes = {node: False for node in g.nodes}

    wait_nodes.append(start_node)
    visited_nodes[start_node] = True

    while wait_nodes:
        current_node = wait_nodes.popleft()
        neighbours = g[current_node]

        for neighbor in neighbours:
            if not visited_nodes[neighbor]:
                wait_nodes.append(neighbor)
                visited_nodes[neighbor] = True
        path_nodes.append(current_node)

    return path_nodes
