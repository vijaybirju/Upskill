class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        n=len(s)
        for i in range(n):
            if s[i]  in count:
                count[s[i]] +=1
            else:
                count[s[i]] = 1
        palindrome=0
        odd_found = False
        for key,value in count.items():
            if value % 2 == 0:
                palindrome+=value
            else:
                palindrome += value - 1 
                odd_found = True 
            
        if odd_found:
            palindrome += 1
        return palindrome

        
