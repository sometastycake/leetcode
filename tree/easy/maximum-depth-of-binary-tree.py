# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        result = 1
        visited = set()
        while stack:
            current, level = stack[-1]
            if current.left and hash(current.left) not in visited:
                stack.append((current.left, level + 1))
            elif current.right and hash(current.right) not in visited:
                stack.append((current.right, level + 1))
            else:
                visited.add(hash(current))
                if level > result:
                    result = level
                stack.pop()
        return result
