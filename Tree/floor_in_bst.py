'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, x):
        #code here
        ans = -1

        while root:

            if root.data == x:
                return root.data

            elif root.data > x:
                root = root.left

            else:
                ans = root.data
                root = root.right

        return ans