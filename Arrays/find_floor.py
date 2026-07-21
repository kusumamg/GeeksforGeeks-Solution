class Solution:
    def findFloor(self, arr, x):
        # code here
        ans=-1
        for i in range(0,len(arr)):
            if arr[i]<=x:
                ans=i
            else:
             break
        return ans