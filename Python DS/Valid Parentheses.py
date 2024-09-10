class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)
        bracket_map = {')': '(', '}': '{', ']': '['}
        for i in range(n):
            if s[i] in bracket_map.values():
                stack.append(s[i])
            else:
                if stack and stack[-1] == bracket_map[s[i]]:
                    stack.pop()
                else:
                    return False
        
        return not stack
            


        
