class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_st  = {}
        mapping_ts  = {}
        for i,element in enumerate(s):
            if element not in mapping_st:
                mapping_st[element] = t[i]
            else:
                if mapping_st[element] != t[i]:
                    return False
        for i,element in enumerate(t):
            if element not in mapping_ts:
                mapping_ts[element] = s[i]
            else:
                if mapping_ts[element] != s[i]:
                    return False
        return True


