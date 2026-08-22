class Solution:
    def sumOfDivisors(self, n):
    	#code here 
        total = 0

        for i in range(1, n + 1):
            total += i * (n // i)

        return total
