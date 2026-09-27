class Solution:
    def segregateElements(self, arr):
        positive = []
        negative = []

        for x in arr:
            if x >= 0:
                positive.append(x)
            else:
                negative.append(x)

        arr[:] = positive + negative
