class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        s = [0] * n
        s[0] = 1
        s[1] = 2

        for i in range(2, n):
            s[i] = s[i-1] + s[i-2]

        return s[n-1]
