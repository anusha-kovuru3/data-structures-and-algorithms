class Solution:
    def secondLargestElement(self, nums):
        first_largest = float('-inf')
        second_largest = float('-inf')

        for i in range(len(nums)):
            if nums[i] > first_largest:
                second_largest = first_largest 
                first_largest = nums[i] 
            elif nums[i] != first_largest and nums[i] > second_largest:
                second_largest = nums[i]

        return -1 if second_largest == float('-inf') else second_largest
        