# https://leetcode.com/problems/count-complete-tree-nodes/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        queue = [root]
        while queue:
            node = queue.pop(0)
            result += 1
            for child in (node.left, node.right):
                if child:
                    queue.append(child)
        return result
