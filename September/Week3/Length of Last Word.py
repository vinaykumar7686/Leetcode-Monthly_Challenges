# Length of Last Word

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''

class Solution0:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        for ch in s[::-1]:
            if len(ch)!=0:
                return len(ch)
        return 0

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        start = True
        for ch in s[::-1]:
            if ch!=" ":
                count+=1
                start = False
            if start and ch == " ":
                continue
            if not start and ch == ' ':
                return count
        return count