# Longest String Chain

'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
   Hide Hint #1  
Instead of adding a character, try deleting a character to form a chain in reverse.
   Hide Hint #2  
For each word in order of length, for each word2 which is word with one character removed, length[word2] = max(length[word2], length[word] + 1).
'''
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        # s1 is original string
        # s2 is predecessor
        
        def isPred(s1, s2):
            s1 = list(s1)
            s2 = list(s2)
            
            count = True
            for ch in s2:
                if ch in s1:
                    s1.remove(ch)
                elif count:
                    count = False
                else:
                    return False
                
            return True
        
        
        hash = dict()
        
        for word in words:
            n = len(word)
            
            if n in hash:
                hash[n].append(word)
            else:
                hash[n] = [word]
                
        
        def recur(i, s, val):
            if i+1 not in hash:
                return val
            else:
                x= 0
                for word in hash[i+1]:
                    if isPred(s, word):
                        recur(i+1, word, val+1)
                    
            
        
        for i in range(sorted(hash.keys())):
            
                    
        return 1
