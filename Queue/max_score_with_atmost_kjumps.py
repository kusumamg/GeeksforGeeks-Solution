from collections import deque

class Solution:
    def getScore(self, arr, k):
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]

        dq = deque([0])

        for i in range(1, n):
            while dq and dq[0] < i - k:
                dq.popleft()

            dp[i] = dp[dq[0]] + arr[i]

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)

        return dp[-1]