class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        char_occurrence = [i for i, char in enumerate(s) if char == c]
        result = []
        for i, char in enumerate(s):
            min_diff = min(abs(i - occ) for occ in char_occurrence)
            result.append(min_diff)
        return result

