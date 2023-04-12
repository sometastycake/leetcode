# https://leetcode.com/problems/symmetric-tree/

from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bfs(self, node: Optional[TreeNode]):
        if not node:
            return []
        queue = [(node, 1)]
        levels = defaultdict(list)
        while queue:
            current, level = queue.pop(0)
            if current:
                levels[level].append(current.val)
            else:
                levels[level].append(None)
                continue
            for subtree in (current.left, current.right):
                if subtree:
                    queue.append((subtree, level + 1))
                else:
                    queue.append((None, level + 1))
        return levels

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_tree_levels = self.bfs(root.left)
        right_tree_levels = self.bfs(root.right)
        if len(left_tree_levels) != len(right_tree_levels):
            return False
        for level in left_tree_levels:
            left_level_values = list(reversed(left_tree_levels[level]))
            right_level_values = right_tree_levels[level]
            if left_level_values != right_level_values:
                return False
        return True
