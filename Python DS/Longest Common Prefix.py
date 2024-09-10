class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_string = strs[0]
        n=len(strs)
        for i in range(1,n):
            current_str = strs[i]
            for j in range(min(len(common_string),len(current_str))):
                if common_string[j] != current_str[j]:
                    common_string = common_string[:j]
                    break
            else:
                common_string = common_string[:min(len(common_string), len(current_str))]
        return common_string

