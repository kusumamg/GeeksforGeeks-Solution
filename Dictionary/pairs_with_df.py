class Solution:
    def countPairs(self, arr, k):
        freq = {}
        count = 0

        for num in arr:
            count += freq.get(num - k, 0)

            if k != 0:
                count += freq.get(num + k, 0)

            freq[num] = freq.get(num, 0) + 1

        return count