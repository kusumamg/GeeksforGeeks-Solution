class Solution:
    def generateParentheses(self, n):
        #code here
        ans=[]
        def backtrack(cur,open_count,close_count):
            if len(cur)==n:
                ans.append(cur)
                return
            if open_count < n // 2:
                backtrack(cur + "(", open_count + 1, close_count)
                
            if close_count<open_count:
                backtrack(cur + ")", open_count, close_count + 1)
        backtrack("",0,0)
        return ans


