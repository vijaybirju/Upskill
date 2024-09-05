class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_magazine = defaultdict(int)
        count_ransom = defaultdict(int)
        for c in magazine:
            count_magazine[c]+=1
        for c in ransomNote:
            count_ransom[c]+=1
        for c in ransomNote:
            if count_ransom[c]>count_magazine[c]:
                return False
        return True

        
