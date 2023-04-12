# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        levels = defaultdict(list)
        queue = [(root, 1)]
        while queue:
            current, level = queue.pop(0)
            levels[level].append(current)
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
        for nodes in levels.values():
            i = 0
            while i + 1 < len(nodes):
                nodes[i].next = nodes[i + 1]
                i += 1
            nodes[-1].next = None
        return root
