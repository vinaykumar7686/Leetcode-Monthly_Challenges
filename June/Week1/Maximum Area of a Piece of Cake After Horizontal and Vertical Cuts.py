# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

'''

Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:



Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
 

Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct.
   Hide Hint #1  
Sort the arrays, then compute the maximum difference between two consecutive elements for horizontal cuts and vertical cuts.
   Hide Hint #2  
The answer is the product of these maximum values in horizontal cuts and vertical cuts.

'''

class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        if not 0 in hc:
            hc.append(0)
        if not 0 in vc:
            vc.append(0)
            
        if not h in hc:
            hc.append(h)
        if not w in vc:
            vc.append(w)
            
        hc.sort()
        vc.sort()
        
        res = 0
        hdiff = 0
        vdiff = 0
        
        for i in range(1, len(hc)):
            
            hdiff = max(hdiff, (hc[i]-hc[i-1]))
            
        for j in range(1, len(vc)):
            
            vdiff = max(vdiff, (vc[j]-vc[j-1]))
                
        res = (hdiff*vdiff)%(10**9 + 7)
        
                
                
        return res

# TLE
class SolutionTLE:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        if not 0 in hc:
            hc.append(0)
        if not 0 in vc:
            vc.append(0)
            
        if not h in hc:
            hc.append(h)
        if not w in vc:
            vc.append(w)
            
        hc.sort()
        vc.sort()
        
        res = 0
        
        for i in range(1, len(hc)):
            
            hdiff = hc[i]-hc[i-1]
            
            for j in range(1, len(vc)):
                
                res = max(res, hdiff*(vc[j]-vc[j-1]))
                
                
        return res
                
                
