class Solution:
    def getSecondLargest(self, arr):
        # code here
       
     arr=list(set(arr))
     if len(arr)<2:
         return -1
     arr.sort()
     return arr[-2]
     