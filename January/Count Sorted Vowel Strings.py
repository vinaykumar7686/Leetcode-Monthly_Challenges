# Count Sorted Vowel Strings

'''

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
 

Constraints:

1 <= n <= 50 
   Show Hint #1  
   Hide Hint #2  
Think backtracking. Build a recursive function count(n, last_character) that counts the number of valid strings of length n and whose first characters are not less than last_character.
   Hide Hint #3  
In this recursive function, iterate on the possible characters for the first character, which will be all the vowels not less than last_character, and for each possible value c, increase the answer by count(n-1, c).
'''

class Solution:
    def __init__(self):
        
        self.count = 0
        # self.vowels = ['a', 'e', 'i', 'o', 'u']
        
    def countVowelStrings(self, n: int) -> int:
        
        
        def helper(s, size):
            
            if size == n:
                self.count+=1
                
            if size>n:
                return
            
            for i in range(s, 5):
                
                helper(i, size+1)
                
        helper(0, 0)
        
        return self.count
