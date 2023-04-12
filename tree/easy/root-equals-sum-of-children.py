# https://leetcode.com/problems/root-equals-sum-of-children/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return root.val == root.left.val + root.right.val
