class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code =  [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res = []
        for  word in words:
            morse= ""
            for char in word:
                morse += morse_code[ord(char)-ord("a")]
            if morse not in res:
                res.append(morse)
        return len(res)
