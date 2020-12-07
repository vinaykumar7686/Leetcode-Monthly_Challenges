# Spiral Matrix II

'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        rowbeg = 0
        rowend = n-1
        
        colbeg = 0
        colend = n-1
        
        ans = [[0 for _ in range(n)] for x in range(n)]
        
        count = 1
        
        while rowbeg<=rowend and colbeg<=colend:
            
            # print(rowbeg, rowend,colbeg,colend)
            
            for i in range(colbeg, colend+1):
                ans[rowbeg][i] = count
                count+=1
                
            rowbeg+=1
            # print(ans)
            
            for i in range(rowbeg, rowend+1):
                ans[i][colend] = count
                count+=1                
                
            colend-=1
            # print(ans)
            
            for i in range(colend, colbeg-1, -1):
                ans[rowend][i] = count
                count+=1
                
            rowend-=1
            # print(ans)
            
            for i in range(rowend, rowbeg-1,-1):
                ans[i][colbeg] = count
                count+=1
                
            colbeg+=1
            # print(ans)
            
        return ans
