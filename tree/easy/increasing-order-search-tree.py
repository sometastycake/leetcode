# https://leetcode.com/problems/increasing-order-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.root = None
        self.tail = None
        self.stack = []
        self.visited = set()

    def addRight(self, node: TreeNode) -> None:
        if self.root is None:
            self.root = self.tail = TreeNode(node.val)
        else:
            self.tail.right = TreeNode(node.val)
            self.tail = self.tail.right
        self.stack.pop()
        self.visited.add(hash(node))

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.stack.append(root)
        while self.stack:
            node = self.stack[-1]
            if node.left and hash(node.left) not in self.visited:
                self.stack.append(node.left)
            elif node.right and hash(node.right) not in self.visited:
                self.addRight(node)
                self.stack.append(node.right)
            else:
                self.addRight(node)
        return self.root
