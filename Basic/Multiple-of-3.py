class Solution:
    def isMultipleOf3(self, s):
        rem = 0

        for bit in s:
            rem = (rem * 2 + int(bit)) % 3

        return rem == 0
