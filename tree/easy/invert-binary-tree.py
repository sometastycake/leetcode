# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        result = TreeNode(root.val)
        queue = [(root, result)]
        while queue:
            node, pointer = queue.pop(0)
            if node.right:
                pointer.left = TreeNode(node.right.val)
                queue.append((node.right, pointer.left))
            if node.left:
                pointer.right = TreeNode(node.left.val)
                queue.append((node.left, pointer.right))
        return result
