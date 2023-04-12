# https://leetcode.com/problems/path-sum/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_leaf(node: TreeNode) -> bool:
    return not node.left and not node.right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        visited = set()
        while stack:
            current, summ = stack[-1]
            if summ == targetSum and is_leaf(current):
                return True
            if current.left and hash(current.left) not in visited:
                stack.append((current.left, summ + current.left.val))
            elif current.right and hash(current.right) not in visited:
                stack.append((current.right, summ + current.right.val))
            else:
                visited.add(hash(current))
                stack.pop()
        return False
