def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = nums1 + nums2
        merged_array.sort()
        if len(merged_array) % 2 == 0:
                middle_index = len(merged_array) // 2
                median = (merged_array[middle_index] + merged_array[middle_index - 1]) / 2.0
        else:
                middle_index = len(merged_array) // 2
                median = float(merged_array[middle_index])
        return (median)
        
nums1 = [1,2,5,7,9]
nums2 = [3,4]
median = findMedianSortedArrays(nums1,nums2)
print(f"median value is {median}")
        