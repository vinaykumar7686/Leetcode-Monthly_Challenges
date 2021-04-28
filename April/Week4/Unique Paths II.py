# Unique Paths II

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

 

Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
   Hide Hint #1  
The robot can only move either down or right. Hence any cell in the first row can only be reached from the cell left to it. However, if any cell has an obstacle, you don't let that cell contribute to any path. So, for the first row, the number of ways will simply be
if obstacleGrid[i][j] is not an obstacle
     obstacleGrid[i,j] = obstacleGrid[i,j - 1] 
else
     obstacleGrid[i,j] = 0
You can do a similar processing for finding out the number of ways of reaching the cells in the first column.
   Hide Hint #2  
For any other cell, we can find out the number of ways of reaching it, by making use of the number of ways of reaching the cell directly above it and the cell to the left of it in the grid. This is because these are the only two directions from which the robot can come to the current cell.
   Hide Hint #3  
Since we are making use of pre-computed values along the iteration, this becomes a dynamic programming problem.
if obstacleGrid[i][j] is not an obstacle
     obstacleGrid[i,j] = obstacleGrid[i,j - 1]  + obstacleGrid[i - 1][j]
else
     obstacleGrid[i,j] = 0
'''

class Solution:
    def uniquePathsWithObstacles(self, arr: List[List[int]]) -> int:
        m = len(arr)
        n = len(arr[0])
        
        if arr[0][0] == 1 or arr[m-1][n-1] == 1:
            return 0
        
        arr[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                if arr[i][j] == 1:
                    arr[i][j] = 0
                    
                else:
                    if i!=0:
                        arr[i][j] = arr[i-1][j]
                        
                    if j!=0:
                        arr[i][j] += arr[i][j-1] 
                        
                        
        return arr[m-1][n-1]
       

# --------------------------------> TLE
class Solution:
    def __init__(self):
        self.count = 0
    def uniquePathsWithObstacles(self, arr: List[List[int]]) -> int:
        
        def recur(i,j,m,n):
            if arr[i][j] == 1:
                return 0
                                
            elif i == m-1 and j == n-1:
                self.count+=1
            
            if i<m-1:
                recur(i+1, j, m, n)
            if j<n-1:
                recur(i, j+1, m, n)
                
        
        recur(0,0,len(arr), len(arr[0]))
        
        return self.count
       
       
'''
SOLUTION

Approach 1: Dynamic Programming
Intuition

The robot can only move either down or right. Hence any cell in the first row can only be reached from the cell left to it.

Current
2 / 4
And, any cell in the first column can only be reached from the cell above it.

Current
3 / 4
For any other cell in the grid, we can reach it either from the cell to left of it or the cell above it.

If any cell has an obstacle, we won't let that cell contribute to any path.

We will be iterating the array from left-to-right and top-to-bottom. Thus, before reaching any cell we would have the number of ways of reaching the predecessor cells. This is what makes it a Dynamic Programming problem. We will be using the obstacleGrid array as the DP array thus not utilizing any additional space.

Note: As per the question, cell with an obstacle has a value 1. We would use this value to make sure if a cell needs to be included in the path or not. After that we can use the same cell to store the number of ways to reach that cell.

Algorithm

If the first cell i.e. obstacleGrid[0,0] contains 1, this means there is an obstacle in the first cell. Hence the robot won't be able to make any move and we would return the number of ways as 0.
Otherwise, if obstacleGrid[0,0] has a 0 originally we set it to 1 and move ahead.
Iterate the first row. If a cell originally contains a 1, this means the current cell has an obstacle and shouldn't contribute to any path. Hence, set the value of that cell to 0. Otherwise, set it to the value of previous cell i.e. obstacleGrid[i,j] = obstacleGrid[i,j-1]
Iterate the first column. If a cell originally contains a 1, this means the current cell has an obstacle and shouldn't contribute to any path. Hence, set the value of that cell to 0. Otherwise, set it to the value of previous cell i.e. obstacleGrid[i,j] = obstacleGrid[i-1,j]
Now, iterate through the array starting from cell obstacleGrid[1,1]. If a cell originally doesn't contain any obstacle then the number of ways of reaching that cell would be the sum of number of ways of reaching the cell above it and number of ways of reaching the cell to the left of it.
 obstacleGrid[i,j] = obstacleGrid[i-1,j] + obstacleGrid[i,j-1]
If a cell contains an obstacle set it to 0 and continue. This is done to make sure it doesn't contribute to any other path.
Following is the animation to explain the algorithm's steps:

Current
17 / 18


Complexity Analysis

Time Complexity: O(M \times N)O(M×N). The rectangular grid given to us is of size M \times NM×N and we process each cell just once.
Space Complexity: O(1)O(1). We are utilizing the obstacleGrid as the DP array. Hence, no extra space.

'''
