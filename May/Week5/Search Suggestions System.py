# Search Suggestions System

## Partially Solved

'''

Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
   Hide Hint #1  
Brute force is a good choice because length of the string is ≤ 1000.
   Hide Hint #2  
Binary search the answer.
   Hide Hint #3  
Use Trie data structure to store the best three matching. Traverse the Trie.

'''

class Solution:
    def __init__(self):
        self.root = {'*':['*', []]}
        
        
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        
        for product in products:
            
            curr = self.root
            tmp = ""
            for ch in product:
                
                if ch not in curr:
                    curr[ch] = [dict(), []]
                    
                curr[ch][1].append(product)
                curr = curr[ch][0]
                
                tmp = ch
                
            curr['*'] = '*'
            
        # print(self.root)
        
        
        res = []
        
        curr = self.root
        for ch in searchWord:
            res.append([])
            
            if ch in curr:
                res[-1].extend(curr[ch][-1][:3])
                curr = curr[ch][0]
                
            '''else:
                break'''
                
        return res
