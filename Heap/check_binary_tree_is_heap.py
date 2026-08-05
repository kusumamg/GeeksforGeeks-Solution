from collections import deque

class Solution:
    def isHeap(self, root):

        if not root:
            return True

        q = deque([root])
        null_seen = False

        while q:
            node = q.popleft()

            if node.left:
                if null_seen or node.left.data > node.data:
                    return False
                q.append(node.left)
            else:
                null_seen = True

            if node.right:
                if null_seen or node.right.data > node.data:
                    return False
                q.append(node.right)
            else:
                null_seen = True

        return True