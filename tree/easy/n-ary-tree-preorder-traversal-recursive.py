# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def solve(self, node: 'Node') -> List[int]:
        if not node.children:
            return [node.val]
        result = [node.val]
        for child in node.children:
            result += self.solve(child)
        return result

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        return self.solve(root)
