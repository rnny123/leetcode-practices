import re
s= "aa"
p = "a"
yeet = re.search(r'a',"aa" )
print(bool(yeet))
#search checks if the pattern 'a*' is present in anywhere in the string "aaaaa hello a my name is"



def isMatch2(s, p):
       if re.match(f"^{p}$", s):
              return True
       else:
              return False

s = "ab"
p = ".*"

print(f"second value is {isMatch2(s,p)}")