class Solution:
    def thirdLargest(self, arr):
        arr.sort(reverse=True)
        return arr[2] if len(arr) >= 3 else -1
