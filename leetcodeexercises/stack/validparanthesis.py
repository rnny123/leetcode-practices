#first algo of stack
#stack is basically like a list
#adding to it and popping, remove most recent if condition reached
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #problem soln: creat hash map that map close brack to open brack
        #pop when a pair is found
        #else add to list
        stack = []
        hash_map = {')':'(', '}':'{',']':'['}
        for values in s:
            if values in hash_map and stack and hash_map[values] == stack[-1]:
                stack.pop()
            else:
                stack.append(values)
        if len(stack) == 0:
            return True
        return False

answer =Solution().isValid("({[]})")
print(f"answer is {answer}")