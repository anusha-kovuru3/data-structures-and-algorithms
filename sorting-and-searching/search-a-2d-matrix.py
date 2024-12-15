class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n =  len(matrix)
        m = len(matrix[0])


        for i in range(n):
            if target <= matrix[i][m - 1]:
                low = 0
                high = m - 1
                while low <= high:
                    mid = low + (high - low) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        low = mid + 1
                    else:
                        high = mid - 1
            
                return False

        return False
    
# TC : O(n * log m)