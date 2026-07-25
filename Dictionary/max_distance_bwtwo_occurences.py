class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        first={}
        ans=0
        for i in range(len(arr)):
            if arr[i]not in first:
                first[arr[i]]=i
            else:
                ans=max(ans,i-first[arr[i]])
        return ans
        