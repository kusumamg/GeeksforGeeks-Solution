class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        def fib(x):
            if x==0:
                return 0
            if x==1:
                return 1
            return fib(x-1)+fib(x-2)
        ans=[]
        for i in range(n):
            ans.append(fib(i))
        return ans