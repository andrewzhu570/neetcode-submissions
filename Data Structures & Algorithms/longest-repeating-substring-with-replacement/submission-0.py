class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1

        res = 0
        left = 0
        char_freq = {}
        max_freq = 0

        for right in range(len(s)):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1
            max_freq = max(max_freq, char_freq[s[right]])

            if (right - left + 1) - max_freq > k:
                char_freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1) 


        return right - left + 1



