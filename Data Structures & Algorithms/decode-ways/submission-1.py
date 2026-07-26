
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        dp.append(1)

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                continue
            
            dp[i] = dp[i + 1]
            if i < len(s)-1:
                if (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                    dp[i] += dp[i+2]
        
        return dp[0]
    