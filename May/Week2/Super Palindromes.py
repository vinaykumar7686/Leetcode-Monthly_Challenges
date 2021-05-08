# Super Palindromes

'''

Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

 

Example 1:

Input: left = "4", right = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
Example 2:

Input: left = "1", right = "2"
Output: 1
 

Constraints:

1 <= left.length, right.length <= 18
left and right consist of only digits.
left and right cannot have leading zeros.
left and right represent integers in the range [1, 1018].
left is less than or equal to right.

'''

class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        
        count = 0
        left = int(left)
        right = int(right)
        
        
        def is_palin(num):
            return str(num) == (str(num))[::-1]
        
        magic = 100000
        
        
        # For EVEN
        
        for i in range(magic):
            
            t = str(i)+str(i)[::-1]
            v = int(t)**2
            
            if v>right:
                break
            
            if v>=left and is_palin(v):
                count+=1  
            
            
        # For ODD
        
        for i in range(magic):
            
            t = str(i)+str(i)[-2::-1]
            v = int(t)**2
            
            if v>right:
                break
            
            if v>=left and is_palin(v):
                count+=1    
                    
                    
        return count
                    

'''
# Solution TLE

class Solution(object):
    def superpalindromesInRange(self, left, right):
        """
        :type left: str
        :type right: str
        :rtype: int
        """
        
        count = 0
        left = int(left)
        right = int(right)
        
        
        def is_palin(num):
            return str(num) == (str(num))[::-1]
        
        lo = int(left**0.5)
        hi = int(right**0.5)
        
        for i in range(lo, hi+1):
            if is_palin(i):
                if is_palin(i**2):
                    count+=1
        
        return count
                    
'''
