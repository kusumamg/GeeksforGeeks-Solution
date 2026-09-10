class Solution:
    def getFirstSetBit(self, n):
        position = 1

        while n > 0:
            if n % 2 == 1:
                return position

            n //= 2
            position += 1

        return 0
