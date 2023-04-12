# https://leetcode.com/problems/clone-graph/

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> Optional['Node']:
        if not node:
            return None
        queue = [node]
        creatednodes = {
            node.val: Node(node.val, [])
        }
        while queue:
            originalPointer = queue.pop(0)
            clonePointer = creatednodes[originalPointer.val]
            for neighbor in originalPointer.neighbors:
                if neighbor.val not in creatednodes:
                    creatednodes[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                clonePointer.neighbors.append(creatednodes[neighbor.val])
        return creatednodes[node.val]
