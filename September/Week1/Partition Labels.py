# Partition Labels

'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
 

   Hide Hint #1  
Try to greedily choose the smallest partition that includes the first letter. If you have something like "abaccbdeffed", then you might need to add b. You can use an map like "last['b'] = 5" to help you expand the width of your partition.
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        flag = {}
        
        for ch in s:
            if ch in dic:
                dic[ch] = dic[ch]+1
            else:
                dic[ch] = 1
                flag[ch] = True
        
        ans = []
        
        n = 0
        for i, ch in enumerate(s):
            n+=1
            if dic[ch]==1:
                dic[ch]=0
                flag[ch] = True                
            
            else:
                dic[ch] = dic[ch]-1
                flag[ch] = False
            
            if not False in flag.values():
                ans.append(n)
                n=0
        return ans