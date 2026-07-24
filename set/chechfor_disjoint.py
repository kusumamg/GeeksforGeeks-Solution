class Solution:
    # Function to check if two arrays are disjoint
    def areDisjoint(self, a, b):
        #code here
        s=set(a)
        for num in s:
            if num in b:
                return False
        return True