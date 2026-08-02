''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def inOrder(self, root):
        # code here
        ans = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            ans.append(node.data)
            inorder(node.right)

        inorder(root)
        return ans