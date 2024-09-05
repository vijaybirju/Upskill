class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0 
        for item in t:
            result^=ord(item)
        for item in s:
            result^=ord(item)
        return chr(result)
