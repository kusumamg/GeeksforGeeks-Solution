from collections import deque

class Solution:
    def bfs(self, adj):
        n = len(adj)
        visited = [False] * n
        ans = []

        q = deque([0])
        visited[0] = True

        while q:
            node = q.popleft()
            ans.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        return ans