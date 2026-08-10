from collections import deque

class Solution:
    def isBipartite(self, V, edges):
        graph = [[] for _ in range(V)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        color = [-1] * V

        for start in range(V):
            if color[start] != -1:
                continue

            color[start] = 0
            q = deque([start])

            while q:
                u = q.popleft()

                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)

                    elif color[v] == color[u]:
                        return False

        return True