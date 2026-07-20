class Solution:
    def getAlternates(self, arr):
        n=len(arr)
        result=[ ]
        for i in range(0,n,2):
            result.append(arr[i])
        return result