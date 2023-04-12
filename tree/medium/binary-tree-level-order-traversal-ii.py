# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 1)]
        levels = defaultdict(list)
        while queue:
            current, level = queue.pop(0)
            levels[level].append(current.val)
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
        sorted_levels = sorted(
            levels.items(),
            key=lambda item: item[0],
            reverse=True,
        )
        return [v for k, v in sorted_levels]
