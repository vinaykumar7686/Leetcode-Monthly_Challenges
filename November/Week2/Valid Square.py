# Valid Square

'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
'''

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(a, b):
            return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
        
        distances = [
            dist(p1,p2),
            dist(p1,p3),
            dist(p1,p4),
            dist(p2,p3),
            dist(p2,p4),
            dist(p3,p4),
        ]
        
        distances.sort()
        
        return 0<distances[0] == distances[1] == distances[1] == distances[3] and distances[4] == distances[5]
