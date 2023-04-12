# https://leetcode.com/problems/range-sum-of-bst/

from queue import Queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = 0
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if low <= node.val <= high:
                result += node.val
            if node.left and low <= node.val:
                queue.put(node.left)
            if node.right and high > node.val:
                queue.put(node.right)
        return result
