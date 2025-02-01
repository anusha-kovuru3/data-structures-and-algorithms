class Solution:
    def secondLargestElement(self, nums):
        firstLargest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > firstLargest:
                firstLargest = nums[i] 
        
        second_largest = float('-inf')
        for i in range(len(nums)):
            if firstLargest != nums[i] and second_largest < nums[i]:
                second_largest = nums[i] 
        

        if second_largest == float('-inf'):
            return -1 
        else:
            return second_largest