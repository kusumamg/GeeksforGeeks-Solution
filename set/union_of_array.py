class Solution:    
    def findUnion(self, a, b):
        # code here
        s=set()
        for num in a:
            s.add(num)
        for num in b:
            s.add(num)
        return sorted(s)
        