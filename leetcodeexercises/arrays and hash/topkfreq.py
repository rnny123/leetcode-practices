def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dictionary = {}
    freq = [[] for i in range(len(nums) +1)]
    answer = []
    for values in nums:
        dictionary[values] = 1 + dictionary.get(values,0)
    #basic hashmap method

    #second is grouping method of mapping num of times to values
    for index, values in dictionary.items():
        freq[values].append(index)
    
    #add to answer
    for i in range(len(freq)-1,0,-1):
        for values in freq[i]:
            answer.append(values)
            if len(answer) == k:
                return answer


nums = [1,1,1,1,2,2,2,3,3,4,5]
k = 2
answer = topKFrequent(nums,k)
print(f"max 2 is {answer}")
# print(f"the k max values are {answer}")
