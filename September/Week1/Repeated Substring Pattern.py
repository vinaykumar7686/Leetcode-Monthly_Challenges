# Repeated Substring Pattern

'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        ss = set(s)
        
        ns = len(ss)
        
        if not ns*2<=n:
            return False
        
        check = False
        subarr = ""
        for i, ch in enumerate(s):
            if ch in ss:
                ss.remove(ch)
            if not ss:
                check = True
                
            subarr = subarr+ch
            
            nsa = len(subarr)
            flag = False
            
            if check and n%nsa==0:
                for j in range(i+1, n, nsa):
                    flag = True
                    if not s[j:j+nsa]==subarr:
                        flag = False
                        break
                if flag:
                    return True
        return False