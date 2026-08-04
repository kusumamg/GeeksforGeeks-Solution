'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrderSuccessor(self, root, k):
        ans = None

        while root:
            if k.data < root.data:
                ans = root
                root = root.left
            else:
                root = root.right

        if ans:
            return ans.data
        return -1