# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(node: TreeNode) -> bool:
    return not node.left and not node.right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 9999999999999999
        queue = [(root, 1)]
        while queue:
            current, level = queue.pop(0)
            if is_leaf(current) and level < result:
                result = level
            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))
        return result
