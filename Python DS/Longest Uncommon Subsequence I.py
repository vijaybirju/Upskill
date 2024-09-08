class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        if a == b:
            return -1  
        else: 
            return max(len_a, len_b)
