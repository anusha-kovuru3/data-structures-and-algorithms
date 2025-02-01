class Solution:
    def largestElement(self, nums):
        nums.sort()
        return nums[-1]
    
    
    