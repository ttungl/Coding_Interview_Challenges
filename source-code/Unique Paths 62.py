# 62. Unique Paths

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # sol 1: DP 1-D
        # time O(n^2); space O(n)
        # runtime: 25ms
        # --
        if not m or not n: 
            return 0
        
        count = [1]*n # keep tracking on paths.

        for i in range(1, m): 
            for j in range(1, n):
                count[j] += count[j-1]
        return count[-1] # res
            
        # sol 2: DP 2-D
        # time O(n^2); space O(n*m)
        # runtime: 32ms
        # --
        if not m or not n: return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1] # res
        
        