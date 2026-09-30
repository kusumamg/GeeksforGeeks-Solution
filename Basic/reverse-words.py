class Solution:
    def reverseWords(self, s):
        words = s.split(".")
        words = [word for word in words if word]
        words.reverse()
        return ".".join(words)
