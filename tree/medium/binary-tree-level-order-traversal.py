# https://leetcode.com/problems/binary-tree-level-order-traversal/

from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = defaultdict(list)
        queue = [(root, 1)]
        while queue:
            current, level = queue.pop(0)
            levels[level].append(current.val)
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
        result = []
        for level in sorted(levels.keys()):
            result.append(levels[level])
        return result
