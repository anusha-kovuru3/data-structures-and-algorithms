class Solution:
    def searchRange(self, arr: List[int], target: int) -> List[int]:
        n = len(arr)
        start = 0
        end = n - 1
        ans = [-1, -1]

        # Finding First Occurance
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == target:
                ans[0] = mid
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
        
        start = 0
        end = n - 1

        # Finding Last Occurance
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == target:
                ans[1] = mid
                start = mid + 1
            elif arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
        
        return ans