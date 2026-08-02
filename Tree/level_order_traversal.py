''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

class Solution:
    def levelOrder(self, root):

        if root is None:
            return []

        ans = []
        q = deque([root])

        while q:
            node = q.popleft()
            ans.append(node.data)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return ans