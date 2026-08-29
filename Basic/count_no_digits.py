class Solution:
    def countDigits(self, n):
        count = 0

        while n > 0:
            n = n // 10
            count += 1

        return count
