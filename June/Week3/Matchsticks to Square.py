# Matchsticks to Square

'''

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
0 <= matchsticks[i] <= 109
   Hide Hint #1  
Treat the matchsticks as an array. Can we split the array into 4 equal halves?
   Hide Hint #2  
Every matchstick can belong to either of the 4 sides. We don't know which one. Maybe try out all options!
   Hide Hint #3  
For every matchstick, we have to try out each of the 4 options i.e. which side it can belong to. We can make use of recursion for this.
   Hide Hint #4  
We don't really need to keep track of which matchsticks belong to a particular side during recursion. We just need to keep track of the length of each of the 4 sides.
   Hide Hint #5  
When all matchsticks have been used we simply need to see the length of all 4 sides. If they're equal, we have a square on our hands!

'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.res = False
        s = sum(matchsticks)
        
        if s%4!=0:
            return False
        
        if max(matchsticks)>s//4:
            return False
        
        def recur(a,b,c,d, nums):
            if not nums:
                if a==b==c==d==s//4:
                    self.res = True
                    return
                    
            elif max([a,b,c,d])>s//4:
                return
            else:
                recur(a+nums[0], b,c,d, nums[1:])
                recur(a, b+nums[0],c,d, nums[1:])
                recur(a, b, c+nums[0],d, nums[1:])
                recur(a, b, c, d+nums[0], nums[1:])
                
        recur(0,0,0,0,matchsticks)
        return self.res
