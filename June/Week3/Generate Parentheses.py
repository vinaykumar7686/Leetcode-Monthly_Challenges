# Generate Parentheses

'''

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

'''

class Solution:
    def __init__(self):
        self.res = []
        
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def recur(s, o, c):
            
            if o == c and o == n:
                self.res.append(s)
            
            if o<n:
                recur(s+"(", o+1, c)
                
            if o>c:
                recur(s+")", o, c+1)
                
        recur("",0,0)
        return self.res
