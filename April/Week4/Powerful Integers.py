# Powerful Integers

'''

Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

 

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
 

Constraints:

1 <= x, y <= 100
0 <= bound <= 106

'''

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        if x==1 and y == 1:
            if bound >= 2:
                return [2]
            else:
                return []

        elif x == 1:
            x,y = y,x
        
        xi = 0
        yi = 0
        
        res = set()
        
        val = 0
        lval = -1
        
        while x**xi+1<=bound:
            
            yi = 0
            val = 0
            lval = -1
            
            while val<=bound:
                val = x**xi + y**yi
                
                if lval == val:
                    break
                
                if val<=bound:
                    res.add(val)
                    lval = val
                    
                yi+=1
                
            xi+=1
            
        return res
