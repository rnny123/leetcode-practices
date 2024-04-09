def isMatch(s, p):
       """
       :type s: str
       :type p: str
       :rtype: bool
       """
       dp = [[False] * (len(p) +1) for i in range(len(s) +1)]
       dp[0][0] = True

       for i in range(1,len(p) +1):
              if p[i-1] == '*':
                     dp[0][i] = dp[0][i-2]

       for i in range(1,len(s)+1):
              for j in range(1, len(p)+1):
                     if s[i-1] == p[j-1] or p[j-1] == '.':
                            dp[i][j] = dp[i-1][j-1]
                     elif p[j-1] == '*':
                            if p[j-2] == s[i-1] or p[j-2] == '.':
                                   dp[i][j] = dp[i-1][j]
                            else:
                                   dp[i][j] = dp[i][j-2]
       return dp[i][j]

value = isMatch("aab","c*a*b")
print(f"value is {value}")
        
            
                
