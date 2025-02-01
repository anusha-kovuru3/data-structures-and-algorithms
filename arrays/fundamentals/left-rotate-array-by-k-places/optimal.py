class Solution:
    def  reverse(self, nums, first, last):
        while first < last:
            temp = nums[first]
            nums[first] = nums[last] 
            nums[last] = temp 
            
            first += 1
            last -= 1

    def rotateArray(self, nums, k):
        n = len(nums)
        k = k % n 

        if k == 0:
            return nums
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
        self.reverse(nums, 0, n - 1)

        return nums
        
