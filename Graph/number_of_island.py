class Solution:
    def countIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        count = 0

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        def dfs(i, j):
            grid[i][j] = 'W'

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (0 <= ni < n and
                    0 <= nj < m and
                    grid[ni][nj] == 'L'):
                    dfs(ni, nj)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L':
                    count += 1
                    dfs(i, j)

        return count