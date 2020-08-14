# Iterator for Combination
'''
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid.
   Hide Hint #1  
Generate all combinations as a preprocessing.
   Hide Hint #2  
Use bit masking to generate all the combinations.
'''

class CombinationIterator:

    def __init__(self, string: str, n: int):
        
        self.ans = []
        def getCombs(s, start):
            if len(s) == n:
                self.ans.append(s)
                return
                
            for i in range(start, len(string)):
                getCombs(s+string[i], i+1)
                
        getCombs("", 0)
        
        

    def next(self) -> str:
        return self.ans.pop(0)
        

    def hasNext(self) -> bool:
        return not len(self.ans)==0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()