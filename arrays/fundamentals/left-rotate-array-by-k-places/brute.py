class Solution:
    def rotateArray(self, nums, k):
        n = len(nums)
        k = k % n 
        temp = []
        for i in range(k + 1):
            temp.append(nums[i])
        
        for i in range(k, n):
            nums[i - k] = nums[i]
        
        for i in range(n - k, n):
            nums[i] = temp[i - (n - k)]
            
        return nums