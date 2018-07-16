class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        bestlength = 0
        chars = dict()
        n = len(s)

        for i in range(n):
            if s[i] in chars and start <= chars[s[i]]:
                start = chars[s[i]] + 1
            else:
                bestlength = max(bestlength, i - start + 1)
            chars[s[i]] = i

        return bestlength
