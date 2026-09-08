import math

class Solution:
    def jugglerSequence(self, n):
        ans = []

        while n != 1:
            ans.append(n)

            if n % 2 == 0:
                n = math.floor(n ** 0.5)
            else:
                n = math.floor(n ** 1.5)

        ans.append(1)

        return ans
