class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return True
            if arr[low] == arr[mid] == arr[high]:
                low = low + 1
                high = high - 1
                continue

            if arr[low] <= arr[mid]:
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif arr[mid] <= arr[high]:
                if arr[mid] < target <= arr[high]:
                    low = mid + 1 
                else:
                    high = mid - 1
            
        return False 
        