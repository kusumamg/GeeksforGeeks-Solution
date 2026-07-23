class Solution:
    def checkPangram(self,s):
        #code here
        letters=set()
        for ch in s.lower():
         if ch.isalpha():
             letters.add(ch)
        return len(letters)==26