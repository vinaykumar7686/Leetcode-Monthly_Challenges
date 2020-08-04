'''
Power of Four

Solution
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

'''
import math
class Solution:

    def isPowerOfFour(self, num: int) -> bool:
        if num<=0:
            return False
        x = math.log(num, 4)
        if int(x) == x:
            return True
        return False
    '''
    def isPowerOfFour(self, num):
        if num<= 0:
            return False
        z = bin(num)[::-1]
        if z.count('1') > 1:
            return False
        p = z.index('1')
        return p % 2 == 0
	
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n%4 == 0:
            n /= 4
        return True if n==1 else False
    '''

    