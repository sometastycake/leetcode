# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        values = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            values.append(node.val)
            for child in (node.left, node.right):
                if child:
                    queue.append(child)
        return list(sorted(values))[k - 1]
