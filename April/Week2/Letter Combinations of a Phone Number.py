# Letter Combinations of a Phone Number

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
'''

class Solution:
    def __init__(self):
        self.res = []
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        keys = ['abc', 'def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        def recur(digs,s):
            if not digs:
                self.res.append(s)
            else:
                n = digs[0]
                digs = digs[1:]
                
                for ch in keys[(int(n))-2]:
                    recur(digs, s+ch)
                    
        
        recur(digits, "")
        return self.res
