class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]
        s = list(s)
        i,j = 0, len(s)-1
        while i<j:
            if s[i].lower() in vowels:
                if s[j].lower() in vowels:
                    s[i], s[j] = s[j], s[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        return "".join(s)
