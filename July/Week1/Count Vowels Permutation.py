# Count Vowels Permutation

'''

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
   Hide Hint #1  
Use dynamic programming.
   Hide Hint #2  
Let dp[i][j] be the number of strings of length i that ends with the j-th vowel.
   Hide Hint #3  
Deduce the recurrence from the given relations between vowels.

'''


class Solution:
    def __init__(self):
        self.count = 0
        
    def countVowelPermutation(self, n: int) -> int:
        foll = {
            '':['a','e','i','o','u'],
            'a':['e'],
            'e':['a', 'i'],
            'i':['a','e','o','u'],
            'o':['i','u'],
            'u':['a']
        }
        
        def recur(s, i):
            if i == n:
                self.count+=1
            else:
                if i == 0:
                    for ch in foll['']:
                        recur(ch,1)
                else:
                    for ch in foll[s[-1]]:
                        recur(s+ch, i+1)
                        
                        
        recur("", 0)
        return self.count%(10**9 + 7)
