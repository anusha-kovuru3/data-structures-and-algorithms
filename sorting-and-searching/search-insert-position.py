class Solution:
    def searchInsert(self, arr: List[int], target: int) -> int:
        low = 0
        high = len(arr) - 1
        ans = len(arr)
        while low <= high:
            mid = high + (low - high) // 2
            if arr[mid] == target:
                ans = mid
                return ans
            elif arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                ans = mid
                high = mid - 1
        
        return ans
