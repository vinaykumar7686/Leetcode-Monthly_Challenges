# Bulls and Cows

'''

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        secret = list(secret)
        guess = list(guess)
        
        n = len(secret)
        
        A = 0
        B = 0
        
        i=0
        
        while i<len(secret):
            
            if secret[i]==guess[i]:
                A+=1
                
                secret.pop(i)
                guess.pop(i)
                
                continue
            
            i+=1
        
        
        for num in guess:
            if num in secret:
                B+=1
                secret.pop(secret.index(num))
                
        print((A,B))
        
        
        return f"{A}A{B}B"


    def getHint_1(self, secret: str, guess: str) -> str:
        '''
        By hashmap
        '''
        import collections
        A = 0
        B = 0
        new_sec = ''
        new_gue = ''
        for i in range(len(guess)):
            if guess[i] != secret[i]:
                new_sec+=secret[i]
                new_gue+=guess[i]
            else:
                A+=1
        count_sec = collections.Counter(new_sec)
        count_gue = collections.Counter(new_gue)
        for k, v in count_gue.items():
            if k in count_sec and v == count_sec[k]:
                B+=v
            else:
                B+=min(v, count_sec[k])
        return str(A)+'A'+str(B)+'B'