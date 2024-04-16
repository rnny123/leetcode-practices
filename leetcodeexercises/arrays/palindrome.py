def removechar(s):
    strip_s = ""
    for values in s:
         print(values)
         if 'a'<=values<='z':
            strip_s += values
    return strip_s
def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new_s = removechar(s)
        print(f"new_s is {new_s}")
        length = 0
        i = 0
        j = len(new_s) -1
        while i<j:
            if new_s[i] == new_s[j]:
                length +=1
            i +=1
            j-=1
        if length == i and i!=0 or len(s.replace(" ","")) == 0:
            return True
        else:
            return False
        
s = "            "
ans = isPalindrome(s)
print(f"answer is {ans}")