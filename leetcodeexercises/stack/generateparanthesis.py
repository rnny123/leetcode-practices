#algo of stack and backtracking
#basically only continue and add '(' or ')' if these two rules are true:
#1. no of 'c' dont exceed n (no of n pairs of paranthesis that you input)
#2. ony add ')' if the no of '(' is more than ')'
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []
        def backtracking(openN, closeN):
            if (openN == n and openN == closeN):
                res.append("".join(stack))
                return 
            
            if (openN < n):
                stack.append('(')
                backtracking(openN+1, closeN)
                stack.pop()    

            if (openN > closeN):
                stack.append(')')
                backtracking(openN, closeN+1)
                stack.pop()
        backtracking(0,0)
        return res

combi = Solution().generateParenthesis(8)
print(f"combinations are {combi}")


