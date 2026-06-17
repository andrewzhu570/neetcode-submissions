class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        i = 0
        j = len(s1)
        while j < len(s2)+1:
            temp = s2[i:j]
            if Counter(s1) == Counter(temp):
                return True
            i += 1
            j += 1
        return False