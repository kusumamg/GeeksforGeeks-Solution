class Solution:
    def dfs(self, adj):
        visited = [False] * len(adj)
        result = []

        def dfs_visit(node):
            visited[node] = True
            result.append(node)

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_visit(neighbor)

        dfs_visit(0)

        return result