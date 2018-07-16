class Solution(object):
    def longestPalindrome(self, s):
        start, stop = 0, 0
        for i in range(len(s)):
            l1 = growPalindrome(i, i, s)
            l2 = growPalindrome(i, i+1, s)
            l = max(l1, l2)

            if l > stop - start:
                start = i - (l - 1) // 2
                stop = i + l // 2
        return s[start:stop+1]



def growPalindrome(l, r, s):
    stop = len(s)
    while l >= 0 and r < stop and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1

