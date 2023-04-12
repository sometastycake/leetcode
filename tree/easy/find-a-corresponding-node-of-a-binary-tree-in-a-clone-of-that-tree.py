# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        clonedQueue = Queue()
        clonedQueue.put(cloned)
        while not clonedQueue.empty():
            node = clonedQueue.get()
            if node.val == target.val:
                return node
            if node.left:
                clonedQueue.put(node.left)
            if node.right:
                clonedQueue.put(node.right)
