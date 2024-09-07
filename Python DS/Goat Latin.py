class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        i = 0 
        res = []

        for word in sentence.split():
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                word = word + "ma" + "a"*(i+1)
            else:
                word = word[1:] + word[0] + "ma" + "a"*(i+1)
            i+=1
            res.append(word)
        return " ".join(res)
                 


        
