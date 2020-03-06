class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp = [0 for j in range(amount + 1)]
        dp[0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] += dp[j - coins[i - 1]]
        return dp[-1]