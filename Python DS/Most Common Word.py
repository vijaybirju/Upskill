class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_str = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        words = normalized_str.split()
        wordCount = {}
        for i in range(len(words)):
            if words[i].lower() not in banned:
                wordCount[words[i].lower()]=wordCount.get(words[i].lower(),0)+1
        max_word = max(wordCount, key=wordCount.get)
        return max_word

        
