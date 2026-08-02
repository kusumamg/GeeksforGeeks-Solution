''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # code here
        ans = []

        def postorder(node):
            if node is None:
                return

            postorder(node.left)
            postorder(node.right)
            ans.append(node.data)

        postorder(root)
        return ans
        