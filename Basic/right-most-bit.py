class Solution:
    def posOfRightMostDiffBit(self, m, n):
        x = m ^ n
        if x == 0:
            return -1

        position = 1

        while x % 2 == 0:
            x //= 2
            position += 1

        return position
