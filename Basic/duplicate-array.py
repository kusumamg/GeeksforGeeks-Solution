class Solution:
    def findDuplicates(self, arr):
        count = {}
        result = []

        for num in arr:
            count[num] = count.get(num, 0) + 1

        for num in count:
            if count[num] == 2:
                result.append(num)

        return result
