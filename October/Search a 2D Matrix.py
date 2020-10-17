# Search a 2D Matrix

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix:
            return False
        
        for i in range(len(matrix)-1):
            if target>=matrix[i][0] and target<=matrix[i+1][0]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == target:
                        return True
            
            if matrix[i][0]>target:
                return False
            
        for num in matrix[-1]:
            if num == target:
                return True
        return False
                    
