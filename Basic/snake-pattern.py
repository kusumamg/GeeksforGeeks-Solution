class Solution:
    def snakePattern(self, matrix):
        ans = []

        for i in range(len(matrix)):
            if i % 2 == 0:
                ans.extend(matrix[i])
            else:
                ans.extend(matrix[i][::-1])

        return ans
