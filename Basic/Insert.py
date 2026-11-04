class Solution:
    def insertInMiddle(self, bound, tag):
        mid = len(bound) // 2
        return bound[:mid] + tag + bound[mid:]
