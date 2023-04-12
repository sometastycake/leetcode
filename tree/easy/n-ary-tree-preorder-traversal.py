# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        visited = set()
        while stack:
            node = stack.pop()
            visited.add(hash(node))
            result.append(node.val)
            for child in node.children[::-1]:
                if hash(child) not in visited:
                    stack.append(child)
        return result
