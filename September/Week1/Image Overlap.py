# Image Overlap

'''
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
'''
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        import numpy as np
        A = np.array(A)
        B = np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps

        
class Solution2:
    def largestOverlap(self, a: List[List[int]], b: List[List[int]]) -> int:
        n = len(a)
        N = (3*n-2)
        arr = [[0]*N]*(n-1)
            
        for i in range(n):
            arr.append([0]*(n-1)+a[i]+[0]*(n-1))
        
        arr.extend([[0]*N]*(n-1))
        
        
        def getdot(i,j,n):
            count = 0
            
            for x in range(n):
                for y in range(n):
                    if b[x][y] == 1 and arr[x+i][y+j] == b[x][y]:
                        count+=1
            return count
                        
                    
        ans = 0
        for i in range(0, N-n+1):
            for j in range(0, N-n+1):
                a = getdot(i,j,n)
                if ans<a:
                    ans = a
                
        return ans
            
        