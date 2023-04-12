# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        result = 1
        queue = [(root, 1)]
        while queue:
            current, level = queue.pop(0)
            if level > result:
                result = level
            for child in current.children or []:
                queue.append((child, level + 1))
        return result
