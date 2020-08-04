'''
Valid Palindrome

Solution
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''t= []
        s = s.lower()
        for ch in s:
            if ch.isalnum():
                t.append(ch)
        return t[::1]==t[::-1]'''
        
        l = 0
        r = len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                if not s[l].lower()==s[r].lower():
                    return False
                l+=1
                r-=1
        return True