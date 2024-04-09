def lengthOfLongestSubstring(s):
    dicts = {}
    longest_l = 0
    start = 0


    for i, value in enumerate(s):
        if value in dicts:
            if dicts[value] + 1 > start:
                start = dicts[value] + 1
            print(f"start is {start} and  i is {i}")
        dicts[value] = i
        if len(s[start:i]) + 1> longest_l:
            longest_l = len(s[start:i]) + 1
    return (longest_l)

length_of = lengthOfLongestSubstring("abba")
print(f"length is {length_of}")        
