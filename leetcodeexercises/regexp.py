import re
s= "aa"
p = "a"
yeet = re.search(r'a*',"aaaaa hello a my name is" )
print(bool(yeet))

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
                                   if dp[i-1][j] == True:
                                          dp[i][j] = dp[i-1][j]
                                   else:
                                          dp[i][j] = dp[i][j-2]
                            else:
                                   dp[i][j] = dp[i][j-2]
       return dp[len(s)][len(p)]

def isMatch2(s, p):
       if re.match(f"^{p}$", s):
              return True
       else:
              return False

s = "ab"
p = ".*"
value = isMatch(s,p)

print(f"value is {value}")
print(f"second value is {isMatch2(s,p)}")
        
            
                
