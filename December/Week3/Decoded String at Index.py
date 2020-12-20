# Decoded String at Index
'''
An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation: 
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation: 
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".
 

Constraints:

2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
It's guaranteed that K is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 2^63 letters.
'''

'''
The code below runs at 100% speed with O(n) time complexity. The idea was to calculate the growing size of the decoded string, and then iterate (backwards) using modulo division to find the position of K within a small section.

When K -> 0 across multiple modulo divisions, we can have two cases:

If the last operation was a repetition, then K corresponded to the last character of the repeated string.
If the last operation added a character, then K exactly matched this character.
In both cases, the first character that we detect (iterating backwards) corresponds to the answer.
Cheers,
'''
class Solution:
    def decodeAtIndex(self, S, K):   
        A = [1] # length of arrays: "leet2code3" -> [1,2,3,4,8,9,10,11,12,36]
        for x in S[1:]:
            # OPTIONAL: Early Stop (avoid repeating the string beyond the position "K")
            if A[-1] >= K : break
            #
            if x.isdigit():
                A.append( A[-1]*int(x) )
            else:
                A.append( A[-1]+1 )
        #
        for i in reversed(range(len(A))):
            K %= A[i]
            if not K and S[i].isalpha():
                return S[i]


'''
# ---------------TLE--------------------
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        
        ans = ""
        S = list(S)
        mul = 1
        while S:
            
            ch = S.pop(0)
            
            if ch.isdigit():
                mul = mul*int(ch)
                
            else:
                ans = ans*mul
                mul = 1
                ans = ans+ch
                
            if len(ans)>=K:
                return ans[K-1]
            
            
        ans = ans*mul
        return ans[K-1]
'''
