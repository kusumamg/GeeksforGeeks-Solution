class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        repeating = 0
        missing = 0

        for i in range(1, n + 1):
            if count.get(i, 0) == 2:
                repeating = i
            elif count.get(i, 0) == 0:
                missing = i

        return [repeating, missing]
