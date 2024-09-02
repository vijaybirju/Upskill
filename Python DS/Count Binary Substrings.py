class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prevCnt, ans =0,0
        i = 0 
        while i < len(s):
            curCnt=1
            while i < len(s)-1 and s[i]==s[i+1]:
                curCnt+=1 
                i+=1 
            if prevCnt>0:
                ans+= min(prevCnt,curCnt)
            i+=1
            prevCnt = curCnt
        return ans
