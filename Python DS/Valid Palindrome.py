class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        i = 0
        n= len(s)-1
        mid = i+len(s)//2
        for j in range(mid+1):
            if i<=n:
                if s[i].lower()==s[n].lower() :
                    i+=1
                    n-=1
                else:
                    return False
            else:
                return True
        return True
                
        
