class Solution:
    def minRemove(self, a, b):
        # code here.
        freq1={}
        freq2={}
        for num in a:
            freq1[num]=freq1.get(num,0)+1
        for num in b:
            freq2[num]=freq2.get(num,0)+1
        ans=0
        for num in freq1:
            if num in freq2:
                ans += min(freq1[num],freq2[num])
        return ans
