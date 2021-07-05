# Reshape the Matrix

'''

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
   Hide Hint #1  
Do you know how 2d matrix is stored in 1d memory? Try to map 2-dimensions into one.
   Hide Hint #2  
M[i][j]=M[n*i+j] , where n is the number of cols. This is the one way of converting 2-d indices into one 1-d index. Now, how will you convert 1-d index into 2-d indices?
   Hide Hint #3  
Try to use division and modulus to convert 1-d index into 2-d indices.
   Hide Hint #4  
M[i] => M[i/n][n%i] Will it result in right mapping? Take some example and check this formula.


'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        
        res = [[0 for i in range(c)] for j in range(r)]
        
        i = 0
        j = 0
        
        for arr in mat:
            for num in arr:
                res[i][j] = num
                j = j+1
                
                if j>=c:
                    j%=c
                    i+=1
                
        return res
