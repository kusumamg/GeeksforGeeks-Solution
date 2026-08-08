from collections import deque

class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        indegree = [0] * V

        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        result = []

        while q:
            node = q.popleft()
            result.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return result