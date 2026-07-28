class Solution:
    def calculateSpan(self, arr):
        # code here
        stack = []
        span = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            if not stack:
                span.append(i+1)
            else:
                span.append(i-stack[-1])
            stack.append(i)
        return span
        