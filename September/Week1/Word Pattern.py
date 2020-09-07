# Word Pattern

'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        pattern = list(pattern)
        
        if len(s)!=len(pattern):
            return False
        
        mem = dict()
        
        for ch,  word in zip(pattern, s):
            print(ch,word)
            if ch in mem:
                if mem[ch]!=word:
                    return False
            else:
                if word in mem.values() :
                    return False
                mem[ch] = word
        return True