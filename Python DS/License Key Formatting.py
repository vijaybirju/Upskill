class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-","")
        s = s.upper()[::-1]
        n= len(s)
        res = []
        for i in range(0,n,k):
            res.append(s[i:i+k]) 
        return "-".join(res)[::-1]


