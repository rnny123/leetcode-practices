def from_middle(s,left,right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1
        return (s[left+1:right])
         
def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        list = ''
        for i in range(len(s)):
            odd_palindrome = from_middle(s,i,i)
            if len(odd_palindrome) > len(list):
                list = odd_palindrome
            even_palindrome = from_middle(s,i,i+1)
            if len(even_palindrome) > len(list):
                list = even_palindrome
            return list
                

value = longestPalindrome("ac")
print(f"final value is:{value}")
                
                        
                        
                                
                

        
                
                
            