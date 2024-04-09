def get_combinations(s):
    value = []
    length = len(s)
    for i in range(1<<length):
        array = []
        for j in range(len(s)):
            if (i&(1<<j)):
                array.append(s[j])
        value.append((array))
    return (value)
sets = get_combinations([1,2,3])
print(f"value is {sets}")
