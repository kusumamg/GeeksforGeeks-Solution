class Solution:
    def minValue(self, a, b):
        values = [a + b, a - b, a * b]

        try:
            values.append(a // b)
        except ZeroDivisionError:
            pass

        return min(values)
