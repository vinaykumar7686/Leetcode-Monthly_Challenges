# Longest Palindrome

'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        
        # Creating dictionary containing the frequency of character
        for ch in s:
            if ch in dic:
                dic[ch] = dic[ch]+1
            else:
                dic[ch] = 1
        
        # extra denotes that do we have any character that can be added at the end into palindrome string without disturbing its palindromic ;) property.
        extra = 0
        
        ans = 0
        # Iterate through the frequencies calculated
        for val in dic.values():
            
            # if frequency of any character is even then it can be used fully to construct a palindrome string
            if not val&1:
                ans+=val
            # if even then only the even part of it could be utilised to form palindrome string and remaining one character could be utilised at the end.
            else:
                extra = 1
                ans+=val-1

        return ans+extra