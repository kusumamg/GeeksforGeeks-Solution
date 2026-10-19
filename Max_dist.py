class Solution:
    def maxDistance(self, arr):
        first = {}
        ans = 0

        for i, num in enumerate(arr):
            if num in first:
                ans = max(ans, i - first[num])
            else:
                first[num] = i

        return ans
