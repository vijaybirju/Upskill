class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_t = defaultdict(int)
        count_s = defaultdict(int)
        if len(s) != len(t):
            return False
        for char in t:
            count_t[char]+=1
        for char in s:
            count_s[char]+=1
        for i,char in enumerate(count_s):
            if count_t[char] != count_s[char] :
                return  False
        return True


        
