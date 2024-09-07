class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j = 0, 0 
        n = len(haystack)
        while i < n:
            if haystack[i] != needle[j]:
                i = i - j + 1
                j = 0
            else:
                j+=1
                i+=1                
            if j == len(needle):
                return i - j 
        return -1
                
            
