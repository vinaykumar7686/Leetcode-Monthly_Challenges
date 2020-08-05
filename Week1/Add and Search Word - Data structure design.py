'''
Add and Search Word - Data structure design

Solution
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''
# Solution that uses much time bu uses 93% less memory than other solution.
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.dict.append(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. less space than 93%
        """
        n = len(word)
        for s in self.dict:
            if len(s) != n:
                continue
            
            flag = True
            for i in range(len(word)):
                if word[i]=='.':
                    continue
                
                if word[i]!=s[i]:
                    flag = False
                    break
                    
            if flag:
                return True
        return False
'''
Memory Optimised Approach
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)
        self.wordSet = set()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if word:
            self.dict[len(word)].append(word)
            self.wordSet.add(word)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. less space than 93%
        """
        n = len(word)
        if n in self.dict:
            if word in self.dict[n]:
                return True
            wlist = self.dict[n]
            for s in wlist:
                flag = True
                for i in range(len(word)):
                    if word[i]=='.':
                        continue
                    if word[i]!=s[i]:
                        flag = False
                        break
                if flag:
                    return True
            return False
'''             
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)