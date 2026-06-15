class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        res = 1
        unique = set()
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        unique.add(s[i])
        while j < len(s) and i < len(s):
            while j < len(s) and s[j] not in unique:
                unique.add(s[j])
                current = (j-i) + 1
                if current > res:
                    res = current
                j += 1
            unique.discard(s[i])
            i += 1
        return res