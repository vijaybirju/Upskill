class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        n = len(s)
        while n > 0:
            if s[n-1]=="":
                n-=1
            else:
                return len(s[n-1])
        
