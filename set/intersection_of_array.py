class Solution:
    def intersect(self, a, b):
        # code here
        s=set(a)
        ans=[]
        
        for num in set(b):
            if num in s:
                ans.append(num)
           
        return sorted(ans)
    