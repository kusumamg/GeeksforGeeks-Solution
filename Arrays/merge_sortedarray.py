class Solution:
    def mergeArrays(self, a, b):
        # code here
       a.extend(b)
       a.sort()
       n=len(a)-len(b)
       m=len(b)
       
       for i in range(m):
          b[i]=a[n+i]
       del a[n:]