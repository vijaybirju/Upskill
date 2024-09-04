class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_mapping = "12210111011122000010020202"
        valid_words= []
        for word in words:
            first_letter_row = row_mapping[ord(word[0].lower())-ord("a")]
            if all(row_mapping[ord(char.lower()) - ord("a")] == first_letter_row for char in word):
                valid_words.append(word)
        return valid_words
                
