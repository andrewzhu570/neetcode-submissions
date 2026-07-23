class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i):
            if i == 0:
                return 0
            if i in memo:
                return memo[i]
            res = float('inf')
            for coin in coins:
                if i - coin >= 0:
                    res = min(res, 1 + dfs(i - coin))
            memo[i] = res
            return res
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins
            