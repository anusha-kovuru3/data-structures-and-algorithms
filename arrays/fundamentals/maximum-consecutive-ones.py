class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        maxi = 0 
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
                if maxi < count:
                    maxi = count 
            elif nums[i] == 0:
                count = 0 

        return maxi