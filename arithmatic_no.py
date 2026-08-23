class Solution:
    def inSequence(self, a, b, c):
        if c == 0:
            return a == b

        return (b - a) % c == 0 and (b - a) // c >= 0
