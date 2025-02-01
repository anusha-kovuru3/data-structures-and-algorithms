class Solution:
    def secondLargestElement(self, nums):
        nums = sorted(nums)
        n = len(nums)
        
        for i in range(n - 2, -1, -1):
            if nums[i] != nums[n - 1]:
                return nums[i]
        
        return -1