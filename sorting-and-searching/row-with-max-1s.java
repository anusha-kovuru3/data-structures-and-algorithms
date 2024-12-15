class Solution {
    public int rowWithMax1s(int arr[][]) {
        // code here
        int n = arr.length;
        int m = arr[0].length;
        
        int j = m - 1;
        int row_index = -1;
        
        for(int i = 0; i < n; i++){
            while(j >= 0 && arr[i][j] == 1){
                row_index = i;
                j -= 1;
            }
            if( j < 0){
                break;
            }
        }
        
        return row_index;
    }
}

// i tried solving the program in python with same logic but i didn't understood why i was not able to pass 1 large testcase, but when i used the same logic in java it succesfully passed all the testcases

// class Solution:
//     def rowWithMax1s(self, arr):
//         # code here

//         Approach - 2
//         n = len(arr)
//         m = len(arr[0])
        
//         j = m - 1
//         row_index = -1
        
//         for i in range(n):
//             while j >= 0 and arr[i][j] == 1:
//                 row_index = i
//                 j -= 1
            
//             if j < 0:
//                 break
        
//         return row_index


// Approach - 1
// n = len(arr)
// m = len(arr[0])

// row_index = -1
// max_count = -1
// for i in range(n):
//     if arr[i][m - 1] == 0:
//         continue
//     low = 0
//     high = m - 1
//     first_occurance_1 = -1
//     while low <= high:
//         mid = low + (high - low) // 2
//         if arr[i][mid] == 1:
//             first_occurance_1 = mid
//             high = mid - 1
//         elif arr[i][mid] == 0:
//             low = mid + 1
        
//     if first_occurance_1 != -1:
//         no_of_ones_in_row = m - first_occurance_1
//         if no_of_ones_in_row > max_count:
//             max_count = no_of_ones_in_row
//             row_index = i
        
// return row_index
