def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        reversed_s = reversed(s)
        for i in range(len(s)):
                for j in range(len(reversed_s)):
                        if s[i] == reversed_s[j]:
                            start = i 
                        while s[i] == reversed_s[j]:
                                i +=1
                                j +=1
                                value = i
                        
                        
                                
                

        
                
                
            