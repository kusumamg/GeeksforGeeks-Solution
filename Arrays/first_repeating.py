class Solution:
    def firstRepeated(self, arr):
        # code here 
        count={}
        for num in arr:
            count[num]=count.get(num,0)+1
            
        for i in range (len(arr)):
            if count[arr[i]]>1:
                return i+1
        return -1