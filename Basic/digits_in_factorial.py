import math

class Solution:
    def digitsInFactorial(self, n):
        return int(math.lgamma(n + 1) / math.log(10)) + 1
