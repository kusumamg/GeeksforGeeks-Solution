class Solution:
    def intersection(self,a, b):
        i = 0
        j = 0
        result = []

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                i += 1

            elif a[i] > b[j]:
                j += 1

            else:
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1

        return result