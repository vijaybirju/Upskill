class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split(" ")
    
        if len(s) != len(pattern):
            return False
        map_pattern = defaultdict(str)
        map_words = defaultdict(str)
        for char, word in zip(pattern,s):
            if char in map_pattern and map_pattern[char] != word:
                return False
            if word in map_words and map_words[word] != char:
                return False
            map_pattern[char] = word
            map_words[word] = char 
        return True
