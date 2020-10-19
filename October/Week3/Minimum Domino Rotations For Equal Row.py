# Minimum Domino Rotations For Equal Row

'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:


Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= A.length == B.length <= 2 * 104
1 <= A[i], B[i] <= 6
'''

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a = A[0]
        b = B[0]
        
        bflag = True
        aflag = True
        
        a_swaps = 0
        b_swaps = 0
        
        asame = 0
        bsame = 0
        
        for i,j in zip(A[1:],B[1:]):
            
            if aflag:
                
                if a in [i,j]:
                    
                    if a!=i:
                        
                        a_swaps+=1
                        
                    if i==j==a:
                        asame +=1
                
                else:
                    
                    aflag = False
                    a_swaps = -1
                    asame = 0
                    
                    
            
            if bflag:
                
                if b in [i,j]:
                    
                    if b != j:
                        
                        b_swaps += 1
                        
                    if b==i==j:
                        bsame+=1
                        
                else:
                    
                    bflag = False
                    b_swaps = -1
                    bsame = 0
        
        
        a_swaps = min(len(A)-a_swaps-asame, a_swaps)
        b_swaps = min(len(B)-b_swaps-bsame, b_swaps)
        
        if aflag and bflag:
            return min(a_swaps,b_swaps)
        
        else:
            return a_swaps if aflag else b_swaps
