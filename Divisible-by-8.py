class Solution:
    def isDivisibleBy8(self, s):
        if len(s) <= 3:
            return int(s) % 8 == 0
        
        return int(s[-3:]) % 8 == 0
