class Solution:
    def checkRecord(self, s: str) -> bool:
        a,l,p=0,0,0
        n=len(s)
        for i in range(n):
            if s[i]=="A":
                a+=1
                if a==2:
                    return False
            if s[i] == "L":
                if i< n-2:
                    if s[i+1]==s[i+2]=="L":
                        return False
        return True   
