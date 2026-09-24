class Solution:
    def boundaryTraversal(self, mat):
        n = len(mat)
        m = len(mat[0])
        ans = []

        # Top row
        for j in range(m):
            ans.append(mat[0][j])

        # Right column
        for i in range(1, n):
            ans.append(mat[i][m - 1])

        # Bottom row
        if n > 1:
            for j in range(m - 2, -1, -1):
                ans.append(mat[n - 1][j])

        # Left column
        if m > 1:
            for i in range(n - 2, 0, -1):
                ans.append(mat[i][0])

        return ans
