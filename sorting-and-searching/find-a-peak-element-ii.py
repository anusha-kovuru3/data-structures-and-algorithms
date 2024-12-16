class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def find_max(arr, col, n):
            max_row = -1
            maxi = float("-inf")
            for i in range(n):
                if arr[i][col] > maxi:
                    maxi = arr[i][col]
                    max_row = i
            
            return max_row

        n = len(mat)
        m = len(mat[0])
        
        low = 0
        high = m - 1
        while low <= high:
            mid = low + (high - low) // 2
            row = find_max(mat, mid, n)
            if mid - 1 > 0:
                left = mat[row][mid - 1]
            else:
                left = -1
            
            if mid + 1 < m:
                right = mat[row][mid + 1]
            else:
                right = -1
            
            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                high = mid - 1
            elif mat[row][mid] < right:
                low = mid + 1
            

        