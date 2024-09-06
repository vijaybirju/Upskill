class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        n = len(columnTitle)
        for i in range(n):
            column_number = column_number * 26 + (ord(columnTitle[i]) - ord('A') + 1)
        return column_number
