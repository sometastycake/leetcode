# https://leetcode.com/problems/search-in-a-binary-search-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        node = root
        while node and node.val != val:
            if val <= node.val:
                node = node.left
            elif val > node.val:
                node = node.right
        return node
