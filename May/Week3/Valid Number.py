# Valid Number

'''
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.

'''

class Solution(object):
    def __init__(self):
        self.ints = ['1','2','3','4','5','6','7','8','9','0']
        self.signs = ['+', '-']
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def isInt(s):
            
            if not s:
                return False
            
            if s[0] in self.signs:
                s = s[1:]
            
            if len(s)==0:
                return False
            
            for ch in s:
                if ch not in self.ints:
                    return False
                
            return True
        
        def isDecimal(s):
            if len(s) == 0:
                return False
            
            if s[0] in self.signs:
                s = s[1:]
            
            n = len(s)
            
            if n<2:
                return False
            
            if '.' not in s:
                return False
            
            if s[-1] =='.':
                for ch in s[:-1]:
                    if ch not in self.ints:
                        return False
                    
                return True
            
            
            elif s[0] == '.':
                for ch in s[1:]:
                    if ch not in self.ints:
                        return False
                
                return True
            
            else:
                dot = 0
                
                if n<3:
                    return False
                
                for ch in s:
                    if ch == '.':
                        dot+=1
                        if dot>1:
                            return False
                        
                    elif ch not in self.ints:
                        return False
                    
                return True
                
        s = s.lower()
        if 'e' in s:
            i = s.index('e')

            if (isDecimal(s[:i]) or isInt(s[:i])) and (isInt(s[i+1:])):
                return True
            else:
                return False

        else:
            if isDecimal(s) or isInt(s):
                return True
            else:
                return False
