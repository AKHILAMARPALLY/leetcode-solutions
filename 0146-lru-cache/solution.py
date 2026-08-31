class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palin = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palin[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or is_palin[i + 1][j - 1]):
                    is_palin[i][j] = True
        
        dp = [0] * n
        for i in range(n):
            if is_palin[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(1, i + 1):
                    if is_palin[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        
        return dp[n - 1]