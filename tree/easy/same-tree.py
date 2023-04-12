# https://leetcode.com/problems/same-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q or not q and p:
            return False
        if not p and not q:
            return True
        queue_p = [p]
        queue_q = [q]
        while queue_p and queue_q:
            np: TreeNode = queue_p.pop(0)
            nq: TreeNode = queue_q.pop(0)
            if np.val != nq.val:
                return False
            if np.left and not nq.left or not np.left and nq.left:
                return False
            if np.right and not nq.right or not np.right and nq.right:
                return False
            for subtree in (np.left, np.right):
                if subtree:
                    queue_p.append(subtree)
            for subtree in (nq.left, nq.right):
                if subtree:
                    queue_q.append(subtree)
        return True
